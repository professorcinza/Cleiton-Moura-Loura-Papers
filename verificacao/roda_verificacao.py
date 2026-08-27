#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runner dos instrumentos de verificação (Fase 2 — evidência datada).
Roda os instrumentos pendentes e grava o registro consolidado em
verificacao/evidencia-<data>.json — a evidência mínima exigida pela spec.
"""
import subprocess
import sys
import datetime
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent

INSTRUMENTOS = [
    ("UMC-002", "umc002_origem.py"),
    ("UMC-003", "umc003_margem.py"),
    ("UMC-006", "umc006_mundo.py"),
    ("UMC-008", "umc008_airgap.py"),
    ("UMC-010", "umc010_autoria.py"),
]

def main():
    registro = {
        "registro": "Evidência datada — instrumentos de verificação UMC (Fase 2)",
        "executado_em": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "resultados": [],
    }
    falhas = 0
    for umc, script in INSTRUMENTOS:
        r = subprocess.run([sys.executable, str(AQUI / script)], capture_output=True, text=True, timeout=300)
        try:
            detalhe = json.loads(r.stdout)
        except json.JSONDecodeError:
            detalhe = {"erro": r.stdout[-800:], "stderr": r.stderr[-800:]}
        ok = r.returncode == 0
        if not ok:
            falhas += 1
        registro["resultados"].append({"item": umc, "status": "PASSA" if ok else "FALHA", "evidencia": detalhe})

    destino = AQUI / ("evidencia-%s.json" % datetime.date.today().isoformat())
    destino.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Registro: %s" % destino)
    for res in registro["resultados"]:
        print("  %s — %s" % (res["item"], res["status"]))
    print("TOTAL: %d PASSA, %d FALHA" % (len(INSTRUMENTOS) - falhas, falhas))
    return 0 if falhas == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
