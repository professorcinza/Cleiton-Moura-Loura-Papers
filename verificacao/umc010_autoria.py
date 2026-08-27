#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instrumento UMC-010 — Autoria aberta.
Verifica: LICENSE presente; git log com nome; nenhum binário sem procedência.
Unidade: booleano por item. Ausência de qualquer um = falha.
Evidência mínima: checagem de procedência registrada.
"""
import subprocess
import sys
import datetime
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ARTEFATO = REPO / "umc-artefact"
# Binários permitidos: nada. .gitignore cobre *.pyc, mas auditamos mesmo assim.
EXCETOS = {".git"}

def git(args):
    return subprocess.run(["git"] + args, cwd=REPO, capture_output=True, text=True, check=True).stdout

def main():
    lic_repo = (REPO / "LICENSE").exists()
    lic_artefato = (ARTEFATO / "LICENSE").exists()
    log = git(["log", "--format=%an|%aI|%h"]).splitlines()
    autores = sorted({l.split("|")[0] for l in log if l.strip()})
    spdx = (ARTEFATO / "LICENSE").read_text(encoding="utf-8")[:400].lower().find("agpl") >= 0 if lic_artefato else False

    binarios = []
    for p in REPO.rglob("*"):
        if not p.is_file() or EXCETOS & set(p.parts):
            continue
        if "__pycache__" in p.parts:
            binarios.append((str(p.relative_to(REPO)), "pyc gerado (coberto por .gitignore? verificar git ls-files)"))
            continue
        try:
            head = p.open("rb").read(1024)
        except OSError:
            continue
        if b"\x00" in head:
            binarios.append((str(p.relative_to(REPO)), "binário rastreado"))

    rastreados = [b for b in binarios if "coberto" not in b[1]]
    ok = lic_repo and lic_artefato and spdx and bool(autores) and not rastreados
    evid = {
        "instrumento": "UMC-010 — Autoria aberta",
        "data_evidencia": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "criterio": "LICENSE presente; git log com nome; nenhum binário rastreado sem procedência",
        "license_repo": lic_repo,
        "license_artefato": lic_artefato,
        "spdx_agpl_no_license_artefato": spdx,
        "autores_no_git_log": autores,
        "commits": len(log),
        "binarios_rastreados": rastreados,
        "status": "PASSA" if ok else "FALHA",
    }
    print(json.dumps(evid, ensure_ascii=False, indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
