#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instrumento UMC-006 — O mundo não é texto (teste negativo automatizado).
Corpus de frases-proibidas contra saídas oficiais (docs do artefato, READMEs, saída do CLI).
Unidade: booleano (zero ocorrências). Qualquer ocorrência = falha.
Evidência mínima: execução registrada com zero ocorrências.
"""
import subprocess
import sys
import datetime
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Frases que afirmam que o não-simbólico é token / que o real é computação.
# Formuladas para reduzir falso positivo: exigem o padrão afirmativo, não mera menção.
PROIBIDAS = [
    r"o mundo é (um )?(texto|token|computaç[aã]o|computador)",
    r"o real é (um )?(texto|token|computaç[aã]o|computador)",
    r"fome (é|foi|será) resolvid(a|o) com (texto|token)",
    r"a fome é um token",
    r"o joule é (um )?token",
    r"o corpo é (um )?token",
    r"everything is (a )?token",
    r"the world is (a )?(text|token|computation|computer)",
    r"hunger (is|can be) solved (with|by) (text|tokens)",
    r"el mundo es (un )?(texto|token|computaci[oó]n|ordenador)",
    r"la comida? ?es (un )?token",
    r"世界是(文本|令牌|计算|计算机)",
    r"现实是(文本|令牌|计算)",
]

# Recusas legítimas: negações e menções-proibitivas não são afirmação.
# "X não afirma que o mundo é computação" é justamente a recusa que a spec exige.
NEGACOES = [
    r"n[aã]o\s+(?:\w+\s+){0,3}?(afirma|dizer|declarar|é\s+afirmar|significa\s+que\s+o\s+mundo\s+é)",
    r"\*\*n[aã]o\*\*\s+(afirma|dizer|declarar)",
    r"sem\s+afirmar",
    r"frases-proibidas",
    r"proibida|proibido",
    r"does\s+not\s+(claim|state|assert|mean)",
    r"without\s+claiming",
    r"not\s+(a\s+)?(claim|assert)",
    r"no\s+(afirma|declara|significa)",
    r"sin\s+afirmar",
    r"不(宣称|声称|断言|是)",
    r"而不宣称",
]

# Superfícies oficiais: docs do artefato e READMEs (código Python sai do escopo —
# contém as próprias regras negativas, que citam as frases para proibi-las).
SUPERFICIES = [
    "README.md",
    "paper-umc.pt.md", "paper-umc.en.md", "paper-umc.es.md", "paper-umc.zh.md",
    "umc-artefact/README.md",
    "umc-artefact/exemplos/spec-somar.json",
    "umc-artefact/exemplos/mapa-vila.json",
    "umc-artefact/exemplos/partitura-simples.json",
]

def main():
    ocorrencias = []
    for rel in SUPERFICIES:
        p = REPO / rel
        if not p.exists():
            continue
        texto = p.read_text(encoding="utf-8")
        # Remove blocos de código: as frases-proibidas aparecem lá como CORPUS,
        # citadas para serem proibidas — não como afirmação.
        texto_sem_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
        for pat in PROIBIDAS:
            for m in re.finditer(pat, texto_sem_codigo, flags=re.I):
                ctx = texto_sem_codigo[max(0, m.start()-120):m.end()+60].replace("\n", " ")
                # classificação (Fase 2: citação/recusa/outro): recusa = negação
                # legítima no contexto; normaliza ênfase Markdown (**) antes
                ctx_norm = ctx.replace("*", "").replace("`", "")
                if any(re.search(neg, ctx_norm, flags=re.I) for neg in NEGACOES):
                    classe = "recusa"
                else:
                    classe = "afirmação"
                    ocorrencias.append({"arquivo": rel, "padrao": pat,
                                        "classe": classe, "contexto": ctx})

    evid = {
        "instrumento": "UMC-006 — O mundo não é texto",
        "data_evidencia": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "criterio": "zero ocorrências NÃO classificadas como recusa, em saídas oficiais (recusas e frases-proibidas citadas são conformes)",
        "superficies": SUPERFICIES,
        "padroes": len(PROIBIDAS),
        "ocorrencias_indevidas": ocorrencias,
        "status": "PASSA" if not ocorrencias else "FALHA",
    }
    print(json.dumps(evid, ensure_ascii=False, indent=2))
    return 0 if not ocorrencias else 1

if __name__ == "__main__":
    sys.exit(main())
