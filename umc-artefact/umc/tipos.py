# -*- coding: utf-8 -*-
"""Tipos simbólicos do artefato mínimo UMC (UMC-005, UMC-011).

Três tipos fora do chat — spec, mapa, partitura — cada um com:
  * encoding finito (JSON canônico),
  * pelo menos uma operação,
  * critério operacional de igualdade (forma canônica).

Three non-chat symbolic types — spec, map, score — each with:
  * finite encoding (canonical JSON),
  * at least one operation,
  * an operational equality criterion (canonical form).

Tres tipos simbólicos fuera del chat — spec, mapa, partitura — cada uno con:
  * encoding finito (JSON canónico),
  * al menos una operación,
  * criterio operacional de igualdad (forma canónica).

三个聊天之外的符号类型——spec、地图、乐谱——每个都有：
  * 有限编码（规范 JSON），
  * 至少一种运算，
  * 操作性相等判据（规范形式）。
"""

import json
from dataclasses import dataclass, field, asdict

# ---------------------------------------------------------------------------
# Critério operacional de igualdade (UMC-011) / equality criterion
# ---------------------------------------------------------------------------

def canonico(obj):
    """Serialização JSON canônica (chaves ordenadas) — o critério de igualdade
    operacional entre duas representações do mesmo tipo.

    Canonical JSON serialization (sorted keys) — the operational equality
    criterion between two representations of the same type.
    """
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _carregar(texto):
    try:
        return json.loads(texto)
    except json.JSONDecodeError as exc:
        raise ValueError(f"encoding inválido / invalid encoding / codificación inválida / 编码无效: {exc}")


# ---------------------------------------------------------------------------
# 1) Spec — especificação estruturada / structured specification
# ---------------------------------------------------------------------------

@dataclass
class Spec:
    """Representação simbólica: uma especificação (interface + pré-condição).

    Encoding: JSON — {"nome", "versao", "interface": [{"nome","tipo","descricao"}],
                      "precondicao"}.
    Operações: validar() (esquema), para_codigo() (em transformacoes.py).
    Igualdade: forma canônica.
    """
    nome: str
    versao: str
    interface: list = field(default_factory=list)
    precondicao: str = ""

    # -- encoding --
    def codificar(self):
        return canonico(asdict(self))

    @staticmethod
    def decodificar(texto):
        d = _carregar(texto)
        if not isinstance(d, dict) or "nome" not in d or "interface" not in d:
            raise ValueError("spec sem nome ou interface / missing name or interface")
        return Spec(nome=str(d["nome"]), versao=str(d.get("versao", "")),
                    interface=list(d.get("interface", [])),
                    precondicao=str(d.get("precondicao", "")))

    # -- operação 1: validar esquema --
    def validar(self):
        """Válida o esquema da spec: campos obrigatórios e tipos permitidos."""
        if not self.nome:
            return False
        tipos_ok = {"str", "int", "float", "bool", "list"}
        for it in self.interface:
            if not isinstance(it, dict):
                return False
            if "nome" not in it or "tipo" not in it:
                return False
            if it.get("tipo") not in tipos_ok:
                return False
        return True

    # -- igualdade operacional --
    def igual(self, outro):
        return self.codificar() == outro.codificar()

    def __str__(self):
        return f"Spec({self.nome} v{self.versao}, {len(self.interface)} itens)"


# ---------------------------------------------------------------------------
# 2) Mapa — mapa estruturado (pontos e vias) / structured map
# ---------------------------------------------------------------------------

@dataclass
class Mapa:
    """Representação simbólica: um mapa (pontos com coordenadas + vias).

    Encoding: JSON — {"pontos": [{"id","x","y"}], "vias": [{"a","b"}]}.
    Operações: rota(a,b) (menor caminho, BFS), distancia(a,b).
    Igualdade: forma canônica.
    """
    pontos: list = field(default_factory=list)
    vias: list = field(default_factory=list)

    def _indice(self, pid):
        for i, p in enumerate(self.pontos):
            if p["id"] == pid:
                return i
        return None

    def _adj(self):
        adj = {p["id"]: [] for p in self.pontos}
        for v in self.vias:
            if v["a"] in adj and v["b"] in adj:
                adj[v["a"]].append(v["b"])
                adj[v["b"]].append(v["a"])
        return adj

    # -- encoding --
    def codificar(self):
        return canonico(asdict(self))

    @staticmethod
    def decodificar(texto):
        d = _carregar(texto)
        if not isinstance(d, dict) or "pontos" not in d or "vias" not in d:
            raise ValueError("mapa sem pontos ou vias / missing points or edges")
        return Mapa(pontos=list(d["pontos"]), vias=list(d["vias"]))

    # -- operação 1: menor caminho (BFS) --
    def rota(self, a, b):
        """Menor caminho (em número de vias) entre dois pontos; None se não houver."""
        if self._indice(a) is None or self._indice(b) is None:
            return None
        if a == b:
            return [a]
        adj = self._adj()
        fila, visitado, anterior = [a], {a}, {a: None}
        for atual in fila:
            for viz in adj.get(atual, []):
                if viz not in visitado:
                    visitado.add(viz)
                    anterior[viz] = atual
                    fila.append(viz)
                    if viz == b:
                        caminho = []
                        passo = b
                        while passo is not None:
                            caminho.append(passo)
                            passo = anterior[passo]
                        return list(reversed(caminho))
        return None

    # -- operação 2: distância euclidiana ao longo do caminho --
    def distancia(self, a, b):
        import math
        cam = self.rota(a, b)
        if cam is None or len(cam) < 2:
            return 0.0 if a == b else None
        coords = {p["id"]: (p["x"], p["y"]) for p in self.pontos}
        total = 0.0
        for u, v in zip(cam, cam[1:]):
            x1, y1 = coords[u]
            x2, y2 = coords[v]
            total += math.hypot(x2 - x1, y2 - y1)
        return round(total, 4)

    # -- igualdade operacional --
    def igual(self, outro):
        return self.codificar() == outro.codificar()

    def __str__(self):
        return f"Mapa({len(self.pontos)} pontos, {len(self.vias)} vias)"


# ---------------------------------------------------------------------------
# 3) Partitura — notação musical simples / simple musical notation
# ---------------------------------------------------------------------------

@dataclass
class Partitura:
    """Representação simbólica: uma partitura (compasso + sequência de notas).

    Encoding: JSON — {"compasso": {"numerador": 4, "denominador": 4},
                      "notas": [{"pitch": "C4", "duracao": 1.0}]}.
    Operações: transpor(n) (semitons), duracao_total().
    Igualdade: forma canônica.
    """
    compasso: dict = field(default_factory=lambda: {"numerador": 4, "denominador": 4})
    notas: list = field(default_factory=list)

    ESCALA = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    @staticmethod
    def _pitch_para_semitom(pitch):
        if len(pitch) < 2:
            raise ValueError(f"pitch inválido / invalid pitch / tono inválido / 音高无效: {pitch}")
        nota = pitch[:-1]
        oitava = int(pitch[-1])
        return oitava * 12 + Partitura.ESCALA.index(nota)

    @staticmethod
    def _semitom_para_pitch(sem):
        oitava, resto = divmod(sem, 12)
        return f"{Partitura.ESCALA[resto]}{oitava}"

    # -- encoding --
    def codificar(self):
        return canonico(asdict(self))

    @staticmethod
    def decodificar(texto):
        d = _carregar(texto)
        if not isinstance(d, dict) or "notas" not in d:
            raise ValueError("partitura sem notas / missing notes")
        return Partitura(compasso=dict(d.get("compasso", {"numerador": 4, "denominador": 4})),
                         notas=list(d["notas"]))

    # -- operação 1: transpor --
    def transpor(self, semitons):
        """Nova partitura transposta em `semitons` (positivo sobe, negativo desce)."""
        novas = []
        for n in self.notas:
            sem = self._pitch_para_semitom(n["pitch"]) + semitons
            novas.append({"pitch": self._semitom_para_pitch(sem), "duracao": float(n["duracao"])})
        return Partitura(compasso=dict(self.compasso), notas=novas)

    # -- operação 2: duração total --
    def duracao_total(self):
        return round(sum(float(n["duracao"]) for n in self.notas), 4)

    # -- igualdade operacional --
    def igual(self, outro):
        return self.codificar() == outro.codificar()

    def __str__(self):
        return f"Partitura({len(self.notas)} notas, {self.duracao_total()} unidades)"
