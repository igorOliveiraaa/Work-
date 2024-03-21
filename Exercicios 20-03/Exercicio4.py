import re

class ValidadorEmail:
    def validar_email(self, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email) is not None

import unittest

class TestValidadorEmail(unittest.TestCase):
    def setUp(self):
        self.validador = ValidadorEmail()

    def test_validar_email(self):
        self.assertTrue(self.validador.validar_email('usuario@example.com'))
        self.assertTrue(self.validador.validar_email('usuario123@example.com'))
        self.assertTrue(self.validador.validar_email('usuario.123@example.com'))
        self.assertTrue(self.validador.validar_email('usuario-123@example.com'))
        self.assertTrue(self.validador.validar_email('usuario_123@example.com'))
        self.assertTrue(self.validador.validar_email('user.name@example.com'))
        self.assertTrue(self.validador.validar_email('user+name@example.com'))
        self.assertFalse(self.validador.validar_email('usuario@example'))
        self.assertFalse(self.validador.validar_email('usuario@.com'))
        self.assertFalse(self.validador.validar_email('usuario@example.'))
        self.assertFalse(self.validador.validar_email('@example.com'))
        self.assertFalse(self.validador.validar_email('usuario@@example.com'))

if __name__ == '__main__':
    unittest.main()
