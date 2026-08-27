# -*- coding: utf-8 -*-
import unittest

from umc.tipos import Spec, Mapa, Partitura
from umc.transformacoes import spec_para_codigo, mapa_para_contrato, partitura_para_esquema


class TestTransformacoes(unittest.TestCase):
    """As três transformações verificáveis da Fase 3: spec→código,
    mapa→contrato, partitura→esquema. Nenhuma exige pesos."""

    def test_spec_para_codigo(self):
        s = Spec(nome="somar", versao="1.0",
                 interface=[{"nome": "a", "tipo": "int", "descricao": "parcela"},
                            {"nome": "b", "tipo": "int", "descricao": "parcela"}],
                 precondicao="a e b inteiros")
        codigo = spec_para_codigo(s)
        self.assertIn("def somar(a: int, b: int):", codigo)
        self.assertIn("Implementa a spec", codigo)
        self.assertIn("a e b inteiros", codigo)

    def test_spec_invalida_nao_gera_codigo(self):
        s = Spec(nome="", versao="1", interface=[])
        with self.assertRaises(ValueError):
            spec_para_codigo(s)

    def test_mapa_para_contrato(self):
        m = Mapa(pontos=[{"id": "A", "x": 0, "y": 0},
                         {"id": "B", "x": 3, "y": 0},
                         {"id": "C", "x": 3, "y": 4}],
                 vias=[{"a": "A", "b": "B"}, {"a": "B", "b": "C"}])
        contrato_pt = mapa_para_contrato(m, "A", "C", idioma="pt")
        self.assertIn("CONTRATO DE PERCURSO", contrato_pt)
        self.assertIn("A → B → C", contrato_pt)
        self.assertIn("7.0", contrato_pt)
        contrato_en = mapa_para_contrato(m, "A", "C", idioma="en")
        self.assertIn("ROUTE AGREEMENT", contrato_en)

    def test_mapa_sem_rota_nao_gera_contrato(self):
        m = Mapa(pontos=[{"id": "A", "x": 0, "y": 0}, {"id": "B", "x": 1, "y": 1}], vias=[])
        with self.assertRaises(ValueError):
            mapa_para_contrato(m, "A", "B")

    def test_partitura_para_esquema(self):
        p = Partitura(notas=[{"pitch": "C4", "duracao": 1.0},
                             {"pitch": "G4", "duracao": 0.5}])
        esquema = partitura_para_esquema(p)
        self.assertIn("2 pulsos", esquema)
        self.assertIn("C4", esquema)
        self.assertIn("G4", esquema)
        self.assertIn("1.5", esquema)  # fim do último pulso
        linhas_pulso = [l for l in esquema.splitlines() if l.startswith("pulso ")]
        self.assertEqual(len(linhas_pulso), 2)


if __name__ == "__main__":
    unittest.main()
