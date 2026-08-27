#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instrumento UMC-002 — Línguas como origem.
Verifica: cada commit que toca conteúdo numa língua toca as quatro (en/pt/es/zh).
Unidade: booleano por commit. Diff monolíngue de conteúdo = falha.
Evidência mínima: git log com as quatro línguas no mesmo commit.
"""
import subprocess
import sys
import datetime
import json

PARES = [
    ("paper-umc.pt.md", "paper-umc.en.md", "paper-umc.es.md", "paper-umc.zh.md"),
]

def git(args):
    return subprocess.run(["git"] + args, capture_output=True, text=True, check=True).stdout

def main():
    log = git(["log", "--format=%h|%an|%aI", "--name-only"])
    blocos = []
    atual = None
    for linha in log.splitlines():
        if "|" in linha and not linha.endswith(".md"):
            partes = linha.split("|", 2)
            if len(partes) == 3:
                atual = {"commit": partes[0], "autor": partes[1], "data": partes[2], "arquivos": []}
                blocos.append(atual)
        elif linha.strip() and atual is not None:
            atual["arquivos"].append(linha.strip())

    resultados = []
    falhas = 0
    for b in blocos:
        arqs = set(b["arquivos"])
        toca_conteudo = any(any(p in arqs for p in par) for par in PARES)
        completo = all(all(p in arqs for p in par) for par in PARES) if toca_conteudo else True
        # exções: README, LICENSE, .gitignore, ci/, verificacao/ não exigem as 4 línguas
        only_meta = arqs and arqs <= {"README.md", "LICENSE", ".gitignore"}
        ok = completo or not toca_conteudo
        if not ok:
            falhas += 1
        resultados.append({
            "commit": b["commit"], "autor": b["autor"], "data": b["data"],
            "toca_paper": toca_conteudo, "quatro_linguas": completo, "ok": ok,
            "arquivos": len(b["arquivos"]),
        })

    evid = {
        "instrumento": "UMC-002 — Línguas como origem",
        "data_evidencia": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds"),
        "criterio": "todo commit que toca paper-umc.{pt,en,es,zh}.md toca as quatro; diff monolíngue de conteúdo = falha",
        "commits_avaliados": len(resultados),
        "falhas": falhas,
        "status": "PASSA" if falhas == 0 else "FALHA",
        "detalhe": resultados,
    }
    print(json.dumps(evid, ensure_ascii=False, indent=2))
    return 0 if falhas == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
