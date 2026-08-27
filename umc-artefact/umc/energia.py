# -*- coding: utf-8 -*-
"""Conta de energia visível do artefato mínimo UMC (UMC-004).

Toda tarefa publica joules (ou proxy medido e datado) com unidade e data.
Aqui o proxy é: tempo de parede × potência nominal declarada (15 W),
registrado como proxy — nunca como medição física real.

Visible energy account of the minimal UMC artefact (UMC-004).
Every task publishes joules (or a measured, dated proxy) with unit and date.
Here the proxy is: wall time × declared nominal power (15 W), recorded as a
proxy — never as a real physical measurement.
"""

import json
import os
import time
from datetime import datetime, timezone

# Potência nominal declarada (proxy). Unidade: watts.
# Declared nominal power (proxy). Unit: watts.
POTENCIA_NOMINAL_W = 15.0
UNIDADE = "J"
NOTA = "proxy: tempo_de_parede_s × 15 W nominal (não é medição física)"


class LogEnergia:
    """Registro JSONL de energia por tarefa, com unidade e data (ISO 8601)."""

    def __init__(self, caminho):
        self.caminho = caminho

    def registrar(self, tarefa, tipo, tempo_s):
        joules = round(float(tempo_s) * POTENCIA_NOMINAL_W, 4)
        parent = os.path.dirname(self.caminho)
        if parent:
            os.makedirs(parent, exist_ok=True)
        entrada = {
            "data": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "tarefa": tarefa,
            "tipo": tipo,
            "tempo_s": round(float(tempo_s), 6),
            "joules": joules,
            "unidade": UNIDADE,
            "nota": NOTA,
        }
        with open(self.caminho, "a", encoding="utf-8") as f:
            f.write(json.dumps(entrada, ensure_ascii=False) + "\n")
        return entrada

    def ler(self):
        if not os.path.exists(self.caminho):
            return []
        saida = []
        with open(self.caminho, encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    saida.append(json.loads(linha))
        return saida


def executar_com_log(log_energia, tarefa, tipo, fn):
    """Executa fn() medindo o tempo de parede e registrando os joules do proxy."""
    inicio = time.perf_counter()
    resultado = fn()
    tempo_s = time.perf_counter() - inicio
    entrada = log_energia.registrar(tarefa, tipo, tempo_s)
    return resultado, entrada
