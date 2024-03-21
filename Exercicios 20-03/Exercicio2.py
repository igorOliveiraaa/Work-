class ConversorMoedas:
    def __init__(self, taxa_dolar_euro, taxa_dolar_real):
        self.taxa_dolar_euro = taxa_dolar_euro
        self.taxa_dolar_real = taxa_dolar_real

    def converter_dolar_para_euro(self, valor_dolar):
        return valor_dolar * self.taxa_dolar_euro

    def converter_euro_para_dolar(self, valor_euro):
        return valor_euro / self.taxa_dolar_euro

    def converter_real_para_dolar(self, valor_real):
        return valor_real / self.taxa_dolar_real

    def converter_dolar_para_real(self, valor_dolar):
        return valor_dolar * self.taxa_dolar_real

import unittest

class TestConversorMoedas(unittest.TestCase):
    def setUp(self):
        self.conversor = ConversorMoedas(0.85, 5.2)

    def test_dolar_para_euro(self):
        self.assertAlmostEqual(self.conversor.converter_dolar_para_euro(100), 85, places=2)
        self.assertAlmostEqual(self.conversor.converter_dolar_para_euro(200), 170, places=2)

    def test_euro_para_dolar(self):
        self.assertAlmostEqual(self.conversor.converter_euro_para_dolar(85), 100, places=2)
        self.assertAlmostEqual(self.conversor.converter_euro_para_dolar(170), 200, places=2)

    def test_real_para_dolar(self):
        self.assertAlmostEqual(self.conversor.converter_real_para_dolar(520), 100, places=2)
        self.assertAlmostEqual(self.conversor.converter_real_para_dolar(1040), 200, places=2)

    def test_dolar_para_real(self):
        self.assertAlmostEqual(self.conversor.converter_dolar_para_real(100), 520, places=2)
        self.assertAlmostEqual(self.conversor.converter_dolar_para_real(200), 1040, places=2)

if __name__ == '__main__':
    unittest.main()
