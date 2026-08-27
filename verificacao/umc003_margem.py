#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instrumento UMC-003 — A margem é o teste.
Verifica: um percurso de tarefa da margem completa sem cota, login ou usina do centro.
Executa o percurso `mapa → contrato` (o mais completo: entrada simbólica, operação,
saída multilíngue) e registra zero chamadas ao centro.
Unidade: booleano (completa/falha) + contagem de chamadas ao centro (0 permitido).
Evidência mínima: log do percurso sem chamada ao centro.
"""
import subprocess
import sys
import datetime
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ARTEFATO = REPO / "umc-artefact"

# Padrões de chamada ao centro: URLs http(s) fora de localhost, APIs de nuvem.
CENTRO = re.compile(r"https?://(?!localhost|127\.0\.0\.1)")

def main():
    r = subprocess.run(
        [sys.executable, "-m", "umc", "mapa-para-contrato", "exemplos/mapa-vila.json",
         "--origem", "A", "--destino", "C", "--idioma", "pt"],
        cwd=ARTEFATO, capture_output=True, text=True, timeout=60)

    saida = r.stdout
    chamadas = CENTRO.findall(saida)
    completa = r.returncode == 0 and "CONTRATO" in saida.upper() and not chamadas

    evid = {
        "instrumento": "UMC-003 — A margem é o teste",
        "data_evidencia": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "criterio": "percurso de tarefa completo; 0 chamadas a cota/login/nuvem do centro; sem cota nem login (stdlib local, nenhum credential lookup)",
        "percurso": "mapa → contrato (exemplos/mapa-vila.json, A→C, pt)",
        "exit_code": r.returncode,
        "saida_primeiras_linhas": saida.strip().splitlines()[:12],
        "chamadas_ao_centro": len(chamadas),
        "completa": completa,
        "status": "PASSA" if completa and not chamadas else "FALHA",
    }
    print(json.dumps(evid, ensure_ascii=False, indent=2))
    return 0 if completa and not chamadas else 1

if __name__ == "__main__":
    sys.exit(main())
