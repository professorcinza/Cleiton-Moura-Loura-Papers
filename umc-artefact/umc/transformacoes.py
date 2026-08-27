# -*- coding: utf-8 -*-
"""Transformações verificáveis do artefato mínimo UMC (Fase 3).

spec → código    (Spec → função Python esqueletal)
mapa → contrato  (Mapa → contrato de percurso)
partitura → esquema (Partitura → diagrama de temporização)

Nenhuma transformação exige pesos treinados (UMC-007: spec antes de pesos).
"""

from .tipos import Spec, Mapa, Partitura

# ---------------------------------------------------------------------------
# spec → código
# ---------------------------------------------------------------------------

def spec_para_codigo(spec):
    """Gera um esqueleto de função Python a partir da spec (spec → código).

    O contrato da spec vira assinatura e docstring; a pré-condição vira
    docstring também. Sem corpo mágico: é esqueleto verificável.
    """
    if not isinstance(spec, Spec):
        raise TypeError("esperava Spec / expected Spec")
    if not spec.validar():
        raise ValueError("spec inválida: não gera código / invalid spec: no code generated")

    params = []
    for it in spec.interface:
        nome = it["nome"]
        tipo = {"str": "str", "int": "int", "float": "float",
                "bool": "bool", "list": "list"}[it["tipo"]]
        params.append(f"{nome}: {tipo}")
    assinatura = ", ".join(params) or "dados: str"

    linhas = [f"def {spec.nome}({assinatura}):",
              f'    """Implementa a spec "{spec.nome}" v{spec.versao}.',
              "",
              "    Interface:"]
    for it in spec.interface:
        linhas.append(f'    - {it["nome"]} ({it["tipo"]}): {it.get("descricao", "")}')
    if spec.precondicao:
        linhas.append("")
        linhas.append(f"    Pré-condição: {spec.precondicao}")
    linhas.append('    """')
    linhas.append("    raise NotImplementedError  # corpo por fazer / body pending")
    return "\n".join(linhas) + "\n"


# ---------------------------------------------------------------------------
# mapa → contrato
# ---------------------------------------------------------------------------

def mapa_para_contrato(mapa, origem, destino, idioma="pt"):
    """Gera um contrato de percurso a partir de um mapa (mapa → contrato).

    O contrato lista os pontos do percurso, a distância calculada e a data.
    Texto em quatro línguas (UMC-002: cada língua é origem, não tradução).
    """
    if not isinstance(mapa, Mapa):
        raise TypeError("esperava Mapa / expected Mapa")
    cam = mapa.rota(origem, destino)
    if cam is None:
        raise ValueError(f"sem rota entre {origem} e {destino} / no route between them")
    dist = mapa.distancia(origem, destino)

    rotulos = {
        "pt":  {"titulo": "CONTRATO DE PERCURSO", "entre": "entre", "e": "e",
                "via": "Via", "distancia": "Distância calculada",
                "data": "Data", "clausula": "As partes acordam o percurso abaixo."},
        "en":  {"titulo": "ROUTE AGREEMENT", "entre": "between", "e": "and",
                "via": "Route", "distancia": "Calculated distance",
                "data": "Date", "clausula": "The parties agree on the route below."},
        "es":  {"titulo": "CONTRATO DE RECORRIDO", "entre": "entre", "e": "y",
                "via": "Recorrido", "distancia": "Distancia calculada",
                "data": "Fecha", "clausula": "Las partes acuerdan el recorrido siguiente."},
        "zh":  {"titulo": "路线协议", "entre": "于", "e": "与",
                "via": "路线", "distancia": "计算距离",
                "data": "日期", "clausula": "双方同意下列路线。"},
    }
    if idioma not in rotulos:
        idioma = "pt"
    r = rotulos[idioma]
    rota = " → ".join(cam)
    hoje = "2026-08-27"
    return (f"{r['titulo']}\n"
            f"{r['entre']} {origem} {r['e']} {destino}\n"
            f"{r['via']}: {rota}\n"
            f"{r['distancia']}: {dist}\n"
            f"{r['data']}: {hoje}\n"
            f"{r['clausula']}\n")


# ---------------------------------------------------------------------------
# partitura → esquema
# ---------------------------------------------------------------------------

def partitura_para_esquema(partitura):
    """Gera um diagrama de temporização (esquema) a partir da partitura
    (partitura → esquema). Cada nota vira um pulso com início e fim.

    O esquema é texto ASCII verificável: tempos de início/fim por pulso.
    """
    if not isinstance(partitura, Partitura):
        raise TypeError("esperava Partitura / expected Partitura")
    if not partitura.notas:
        raise ValueError("partitura vazia / empty score")

    linhas = []
    t = 0.0
    for i, n in enumerate(partitura.notas, start=1):
        inicio = round(t, 4)
        fim = round(t + float(n["duracao"]), 4)
        largura = max(1, int(round(float(n["duracao"]) * 4)))
        linhas.append(f"pulso {i:>2} | {n['pitch']:<3} | início={inicio:>6} fim={fim:>6} | {'#' * largura}")
        t = fim
    cabecalho = (f"ESQUEMA DE TEMPORIZAÇÃO — {len(partitura.notas)} pulsos, "
                 f"duração total {partitura.duracao_total()} unidades\n")
    return cabecalho + "\n".join(linhas) + "\n"
