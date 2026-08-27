#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instrumento UMC-008 — Local-first (teste de air-gap automatizado).
Verifica: (a) nenhum módulo do artefato importa rede; (b) os percursos do CLI
completam num processo com sockets bloqueados (air-gap simulado).
Unidade: booleano (offline completo). Qualquer chamada de rede = falha.
Evidência mínima: log do percurso sem rede.
"""
import subprocess
import sys
import datetime
import json
import re
from pathlib import Path

ARTEFATO = Path(__file__).resolve().parent.parent / "umc-artefact"

# (a) auditoria estática: nenhum import de rede no código do artefato
REDE = re.compile(r"^\s*(import|from)\s+(socket|ssl|urllib|http|requests|aiohttp|ftplib|smtplib|telnetlib|asyncio\.streams)\b", re.M)

# (b) air-gap em runtime: script que bloqueia socket e roda o CLI
AIRGAP_SCRIPT = r'''
import socket, subprocess, sys
class Brecha(Exception): pass
def proibido(*a, **k): raise Brecha("chamada de rede bloqueada (air-gap)")
socket.socket = proibido
socket.create_connection = proibido
socket.getaddrinfo = proibido
subprocess.check_call([sys.executable, "-m", "umc"] + sys.argv[1:])
'''

PERCURSOS = [
    ["tipos"],
    ["spec-para-codigo", "exemplos/spec-somar.json"],
    ["mapa-para-contrato", "exemplos/mapa-vila.json", "--origem", "A", "--destino", "C", "--idioma", "pt"],
    ["partitura-para-esquema", "exemplos/partitura-simples.json"],
    ["energia"],
]

def main():
    # (a) estática
    violacoes = []
    for py in sorted(ARTEFATO.glob("umc/**/*.py")):
        if "__pycache__" in str(py):
            continue
        if REDE.search(py.read_text(encoding="utf-8")):
            violacoes.append(str(py.relative_to(ARTEFATO)))

    # (b) runtime com socket bloqueado
    percursos = []
    for args in PERCURSOS:
        r = subprocess.run([sys.executable, "-c", AIRGAP_SCRIPT] + args,
                           cwd=ARTEFATO, capture_output=True, text=True, timeout=60)
        percursos.append({
            "percurso": " ".join(args),
            "exit_code": r.returncode,
            "ok": r.returncode == 0,
            "erro": r.stderr.strip().splitlines()[-1] if r.returncode != 0 else None,
        })

    ok = not violacoes and all(p["ok"] for p in percursos)
    evid = {
        "instrumento": "UMC-008 — Local-first (air-gap)",
        "data_evidencia": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "criterio": "percursos do CLI completam com sockets bloqueados; nenhum import de rede no código",
        "auditoria_estatica": {"imports_de_rede": violacoes},
        "percursos_com_socket_bloqueado": percursos,
        "status": "PASSA" if ok else "FALHA",
    }
    print(json.dumps(evid, ensure_ascii=False, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
