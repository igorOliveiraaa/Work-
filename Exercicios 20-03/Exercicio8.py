import re

def validar_numero_telefone(numero):
    regex = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    return bool(re.match(regex, numero))

import unittest

class TestValidadorTelefone(unittest.TestCase):
    def test_validar_numero_telefone(self):
        self.assertTrue(validar_numero_telefone('(11) 1234-5678'))
        self.assertTrue(validar_numero_telefone('(21) 98765-4321'))
        self.assertFalse(validar_numero_telefone('11 1234-5678')) 
        self.assertFalse(validar_numero_telefone('(11) 12345-678')) 
        self.assertFalse(validar_numero_telefone('(11) 1234-56789')) 
        self.assertFalse(validar_numero_telefone('ABC123')) 

if __name__ == '__main__':
    unittest.main()
