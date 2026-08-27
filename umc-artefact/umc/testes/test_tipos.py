# -*- coding: utf-8 -*-
import unittest

from umc.tipos import Spec, Mapa, Partitura, canonico


class TestEncodingRoundtrip(unittest.TestCase):
    """Encoding finito + decodificação sem perda (UMC-011)."""

    def test_spec_roundtrip(self):
        s = Spec(nome="somar", versao="1.0",
                 interface=[{"nome": "a", "tipo": "int", "descricao": "primeira parcela"}],
                 precondicao="a e b inteiros")
        t = Spec.decodificar(s.codificar())
        self.assertTrue(s.igual(t))

    def test_mapa_roundtrip(self):
        m = Mapa(pontos=[{"id": "A", "x": 0, "y": 0}, {"id": "B", "x": 3, "y": 4}],
                 vias=[{"a": "A", "b": "B"}])
        m2 = Mapa.decodificar(m.codificar())
        self.assertTrue(m.igual(m2))

    def test_partitura_roundtrip(self):
        p = Partitura(notas=[{"pitch": "C4", "duracao": 1.0}, {"pitch": "E4", "duracao": 0.5}])
        p2 = Partitura.decodificar(p.codificar())
        self.assertTrue(p.igual(p2))

    def test_ordem_das_chaves_nao_importa(self):
        a = Mapa(pontos=[{"id": "A", "x": 1, "y": 2}], vias=[])
        b = Mapa(pontos=[{"y": 2, "id": "A", "x": 1}], vias=[])
        self.assertTrue(a.igual(b))


class TestIgualdadeOperacional(unittest.TestCase):
    """Critério operacional de igualdade: forma canônica (UMC-011)."""

    def test_diferentes_sao_diferentes(self):
        s1 = Spec(nome="a", versao="1", interface=[], precondicao="")
        s2 = Spec(nome="a", versao="2", interface=[], precondicao="")
        self.assertFalse(s1.igual(s2))

    def test_canonico_e_deterministico(self):
        obj = {"b": 1, "a": [2, 3], "c": {"z": 1, "y": 2}}
        self.assertEqual(canonico(obj), canonico(obj))


class TestOperacoes(unittest.TestCase):
    """Pelo menos uma operação por tipo (UMC-005/011)."""

    def test_spec_validar(self):
        ok = Spec(nome="somar", versao="1", interface=[{"nome": "a", "tipo": "int"}])
        self.assertTrue(ok.validar())
        ruim = Spec(nome="", versao="1", interface=[])
        self.assertFalse(ruim.validar())

    def test_mapa_rota_e_distancia(self):
        m = Mapa(pontos=[{"id": "A", "x": 0, "y": 0},
                         {"id": "B", "x": 3, "y": 0},
                         {"id": "C", "x": 3, "y": 4}],
                 vias=[{"a": "A", "b": "B"}, {"a": "B", "b": "C"}])
        self.assertEqual(m.rota("A", "C"), ["A", "B", "C"])
        self.assertEqual(m.distancia("A", "C"), 7.0)  # 3 + 4
        self.assertIsNone(m.rota("A", "X"))

    def test_partitura_transpor_e_duracao(self):
        p = Partitura(notas=[{"pitch": "C4", "duracao": 1.0}, {"pitch": "E4", "duracao": 0.5}])
        p2 = p.transpor(2)
        self.assertEqual(p2.notas[0]["pitch"], "D4")
        self.assertEqual(p.duracao_total(), 1.5)


if __name__ == "__main__":
    unittest.main()
