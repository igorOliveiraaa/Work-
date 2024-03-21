import re

class VerificadorSenhaSegura:
    def __init__(self, comprimento_minimo=8):
        self.comprimento_minimo = comprimento_minimo

    def verificar_comprimento(self, senha):
        return len(senha) >= self.comprimento_minimo

    def verificar_maiusculas(self, senha):
        return bool(re.search(r'[A-Z]', senha))

    def verificar_minusculas(self, senha):
        return bool(re.search(r'[a-z]', senha))

    def verificar_especiais(self, senha):
        return bool(re.search(r'[!@#$%^&*()_+{}|:"<>?`\-=[]\;\',./]', senha))

    def verificar_senha_segura(self, senha):
        return (
            self.verificar_comprimento(senha) and
            self.verificar_maiusculas(senha) and
            self.verificar_minusculas(senha) and
            self.verificar_especiais(senha)
        )

import unittest

class TestVerificadorSenhaSegura(unittest.TestCase):
    def setUp(self):
        self.verificador = VerificadorSenhaSegura()

    def test_comprimento_minimo(self):
        self.assertFalse(self.verificador.verificar_comprimento('pass'))
        self.assertTrue(self.verificador.verificar_comprimento('password'))

    def test_maiusculas(self):
        self.assertFalse(self.verificador.verificar_maiusculas('password'))
        self.assertTrue(self.verificador.verificar_maiusculas('Password'))

    def test_minusculas(self):
        self.assertFalse(self.verificador.verificar_minusculas('PASSWORD'))
        self.assertTrue(self.verificador.verificar_minusculas('password'))

    def test_especiais(self):
        self.assertFalse(self.verificador.verificar_especiais('password123'))
        self.assertTrue(self.verificador.verificar_especiais('password@123'))

    def test_senha_segura(self):
        self.assertFalse(self.verificador.verificar_senha_segura('pass'))
        self.assertFalse(self.verificador.verificar_senha_segura('Password'))
        self.assertFalse(self.verificador.verificar_senha_segura('password123'))
        self.assertFalse(self.verificador.verificar_senha_segura('PASSWORD@'))
        self.assertTrue(self.verificador.verificar_senha_segura('P@ssw0rd'))

if __name__ == '__main__':
    unittest.main()
