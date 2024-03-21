class SistemaReservas:
    def __init__(self):
        self.voos_disponiveis = {}
        self.reservas = {}

    def adicionar_voo(self, numero_voo, origem, destino, data, assentos_disponiveis):
        self.voos_disponiveis[numero_voo] = {'origem': origem, 'destino': destino, 'data': data, 'assentos_disponiveis': assentos_disponiveis}

    def pesquisar_voos(self, origem, destino, data):
        voos_encontrados = []
        for numero_voo, voo in self.voos_disponiveis.items():
            if voo['origem'] == origem and voo['destino'] == destino and voo['data'] == data:
                voos_encontrados.append((numero_voo, voo))
        return voos_encontrados

    def fazer_reserva(self, numero_voo, assentos):
        if numero_voo in self.voos_disponiveis and self.voos_disponiveis[numero_voo]['assentos_disponiveis'] >= assentos:
            if numero_voo not in self.reservas:
                self.reservas[numero_voo] = assentos
            else:
                self.reservas[numero_voo] += assentos
            self.voos_disponiveis[numero_voo]['assentos_disponiveis'] -= assentos
            return True
        return False

    def visualizar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, numero_voo, assentos):
        if numero_voo in self.reservas and self.reservas[numero_voo] >= assentos:
            self.reservas[numero_voo] -= assentos
            self.voos_disponiveis[numero_voo]['assentos_disponiveis'] += assentos
            return True
        return False

import unittest

class TestSistemaReservas(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaReservas()
        self.sistema.adicionar_voo('V001', 'São Paulo', 'Rio de Janeiro', '2024-04-01', 100)

    def test_pesquisar_voos(self):
        resultado = self.sistema.pesquisar_voos('São Paulo', 'Rio de Janeiro', '2024-04-01')
        self.assertEqual(resultado, [('V001', {'origem': 'São Paulo', 'destino': 'Rio de Janeiro', 'data': '2024-04-01', 'assentos_disponiveis': 100})])

    def test_fazer_reserva(self):
        self.assertTrue(self.sistema.fazer_reserva('V001', 2))
        self.assertEqual(self.sistema.visualizar_reservas(), {'V001': 2})

    def test_cancelar_reserva(self):
        self.sistema.fazer_reserva('V001', 2)
        self.assertTrue(self.sistema.cancelar_reserva('V001', 1))
        self.assertEqual(self.sistema.visualizar_reservas(), {'V001': 1})

if __name__ == '__main__':
    unittest.main()
