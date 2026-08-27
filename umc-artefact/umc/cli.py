# -*- coding: utf-8 -*-
"""Interface de linha de comando do artefato mínimo UMC.

UMC-009: o artefato chama-se UMC; LLM não aparece fora de citação/recusa.
UMC-008: local-first — stdlib apenas, nenhuma chamada de rede.
"""

import argparse
import json
import sys

from . import __versao__, __data__, __licenca__
from .tipos import Spec, Mapa, Partitura
from .transformacoes import spec_para_codigo, mapa_para_contrato, partitura_para_esquema
from .energia import LogEnergia, executar_com_log

LOG_PADRAO = "logs/energia.jsonl"

CABECALHO = (
    "UMC — Modelo Universal Computacional / Universal Computational Model\n"
    "Artefato mínimo 0.1.0 · 2026-08-27 · AGPL-3.0-or-later\n"
    "Sem pesos. Sem rede. Local-first (UMC-008). Conta de energia visível (UMC-004).\n"
)


def _ler_tipo(classe, caminho):
    with open(caminho, encoding="utf-8") as f:
        return classe.decodificar(f.read())


def _main(argv=None):
    parser = argparse.ArgumentParser(
        prog="umc",
        description=(
            "UMC — Modelo Universal Computacional / Universal Computational Model.\n"
            "Artefato mínimo verificável: spec, mapa e partitura fora do chat.\n"
            "Minimal verifiable artefact: spec, map and score beyond chat.\n"
            "Artefacto mínimo verificable: spec, mapa y partitura fuera del chat.\n"
            "最小可核验制品：聊天之外的 spec、地图与乐谱。"
        ),
    )
    parser.add_argument("--log", default=LOG_PADRAO,
                        help="caminho do log de energia (JSONL) / energy log path")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_spec = sub.add_parser("spec-para-codigo", help="spec → código")
    p_spec.add_argument("arquivo", help="JSON da spec / spec JSON")

    p_mapa = sub.add_parser("mapa-para-contrato", help="mapa → contrato")
    p_mapa.add_argument("arquivo", help="JSON do mapa / map JSON")
    p_mapa.add_argument("--origem", required=True, help="ponto de origem / origin point")
    p_mapa.add_argument("--destino", required=True, help="ponto de destino / destination point")
    p_mapa.add_argument("--idioma", default="pt", choices=["pt", "en", "es", "zh"],
                        help="língua do contrato / contract language")

    p_par = sub.add_parser("partitura-para-esquema", help="partitura → esquema")
    p_par.add_argument("arquivo", help="JSON da partitura / score JSON")

    p_tipos = sub.add_parser("tipos", help="lista os tipos simbólicos (UMC-005/011)")
    p_energia = sub.add_parser("energia", help="mostra o log de energia (UMC-004)")

    args = parser.parse_args(argv)
    sys.stdout.write(CABECALHO + "\n")

    log = LogEnergia(args.log)

    if args.comando == "spec-para-codigo":
        spec = _ler_tipo(Spec, args.arquivo)
        resultado, energia = executar_com_log(
            log, "spec-para-codigo", "spec", lambda: spec_para_codigo(spec))
        sys.stdout.write(resultado + "\n")

    elif args.comando == "mapa-para-contrato":
        mapa = _ler_tipo(Mapa, args.arquivo)
        resultado, energia = executar_com_log(
            log, "mapa-para-contrato", "mapa",
            lambda: mapa_para_contrato(mapa, args.origem, args.destino, args.idioma))
        sys.stdout.write(resultado + "\n")

    elif args.comando == "partitura-para-esquema":
        partitura = _ler_tipo(Partitura, args.arquivo)
        resultado, energia = executar_com_log(
            log, "partitura-para-esquema", "partitura",
            lambda: partitura_para_esquema(partitura))
        sys.stdout.write(resultado + "\n")

    elif args.comando == "tipos":
        sys.stdout.write(
            "Tipos simbólicos (UMC-005/011) — encoding finito + operação + igualdade:\n"
            "  spec      → operação: validar;          igualdade: forma canônica\n"
            "  mapa      → operações: rota, distancia;  igualdade: forma canônica\n"
            "  partitura → operações: transpor, duracao; igualdade: forma canônica\n")
        energia = None

    elif args.comando == "energia":
        entradas = log.ler()
        if not entradas:
            sys.stdout.write("Log de energia vazio / empty energy log.\n")
        else:
            for e in entradas:
                sys.stdout.write(
                    f"{e['data']} | {e['tarefa']} ({e['tipo']}) | "
                    f"{e['joules']} {e['unidade']} | {e['tempo_s']} s\n")
        energia = None

    if energia:
        sys.stdout.write(
            f"[energia] {energia['tarefa']}: {energia['joules']} {energia['unidade']} "
            f"({energia['tempo_s']} s, {energia['data']}, {energia['nota']})\n")


def main():
    _main()


if __name__ == "__main__":
    main()
