# -*- coding: utf-8 -*-
import os
import tempfile
import unittest

from umc.energia import LogEnergia, POTENCIA_NOMINAL_W


class TestEnergia(unittest.TestCase):
    """Conta de energia visível (UMC-004): unidade e data por tarefa."""

    def test_registro_tem_unidade_e_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = LogEnergia(os.path.join(tmp, "energia.jsonl"))
            entrada = log.registrar("spec-para-codigo", "spec", 0.2)
            self.assertEqual(entrada["unidade"], "J")
            self.assertIn("T", entrada["data"])  # ISO 8601 com data e hora
            self.assertAlmostEqual(entrada["joules"], 0.2 * POTENCIA_NOMINAL_W, places=4)
            # persiste em JSONL
            lidas = log.ler()
            self.assertEqual(len(lidas), 1)
            self.assertEqual(lidas[0]["tarefa"], "spec-para-codigo")

    def test_varias_tarefas_acumulam(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = LogEnergia(os.path.join(tmp, "energia.jsonl"))
            log.registrar("a", "spec", 0.1)
            log.registrar("b", "mapa", 0.2)
            self.assertEqual(len(log.ler()), 2)


if __name__ == "__main__":
    unittest.main()
