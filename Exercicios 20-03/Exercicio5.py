def ordenar_crescente(lista):
    return sorted(lista)

def ordenar_decrescente(lista):
    return sorted(lista, reverse=True)

import unittest

class TestOrdenacao(unittest.TestCase):
    def test_ordenar_crescente(self):
        lista = [5, 2, 8, 1, 6]
        self.assertEqual(ordenar_crescente(lista), [1, 2, 5, 6, 8])

    def test_ordenar_decrescente(self):
        lista = [5, 2, 8, 1, 6]
        self.assertEqual(ordenar_decrescente(lista), [8, 6, 5, 2, 1])

if __name__ == '__main__':
    unittest.main()
