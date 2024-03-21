def contar_palavras(texto):
    for pontuacao in '.,!?;:':
        texto = texto.replace(pontuacao, ' ')

    palavras = texto.split()
    
    return len(palavras)

import unittest

class TestContadorPalavras(unittest.TestCase):
    def test_contagem_palavras(self):
        texto1 = "Isso é um teste."
        self.assertEqual(contar_palavras(texto1), 4)

        texto2 = "Olá, mundo! Este é um teste."
        self.assertEqual(contar_palavras(texto2), 6)

        texto3 = "12345"
        self.assertEqual(contar_palavras(texto3), 1)

        texto4 = ""
        self.assertEqual(contar_palavras(texto4), 0)

if __name__ == '__main__':
    unittest.main()
