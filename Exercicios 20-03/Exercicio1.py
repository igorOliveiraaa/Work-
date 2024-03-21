def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

import unittest

class TestCalculadora(unittest.TestCase):
    def test_adicao(self):
        self.assertEqual(adicao(3, 5), 8)
        self.assertEqual(adicao(-1, 1), 0)
        self.assertEqual(adicao(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(-1, 1), -2)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 5), 15)
        self.assertEqual(multiplicacao(-1, 1), -1)
        self.assertEqual(multiplicacao(0, 0), 0)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)
        self.assertEqual(divisao(5, 2), 2.5)
        self.assertRaises(ValueError, divisao, 10, 0)

if __name__ == '__main__':
    unittest.main()
