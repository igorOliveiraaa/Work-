from datetime import datetime

def diferenca_entre_datas(data1, data2):
    data1_obj = datetime.strptime(data1, '%Y-%m-%d %H:%M:%S')
    data2_obj = datetime.strptime(data2, '%Y-%m-%d %H:%M:%S')

    diferenca = data2_obj - data1_obj

    diferenca_em_dias = diferenca.days
    diferenca_em_meses = diferenca_em_dias // 30
    diferenca_em_anos = diferenca_em_dias // 365
    diferenca_em_horas = diferenca.seconds // 3600
    diferenca_em_minutos = (diferenca.seconds % 3600) // 60

    return diferenca_em_dias, diferenca_em_meses, diferenca_em_anos, diferenca_em_horas, diferenca_em_minutos

import unittest

class TestDiferencaDatas(unittest.TestCase):
    def test_diferenca_datas(self):
        data1 = '2023-03-20 12:00:00'
        data2 = '2024-03-21 14:30:00'

        dif_dias, dif_meses, dif_anos, dif_horas, dif_minutos = diferenca_entre_datas(data1, data2)

        self.assertEqual(dif_dias, 366)
        self.assertEqual(dif_meses, 12)
        self.assertEqual(dif_anos, 1)
        self.assertEqual(dif_horas, 2)
        self.assertEqual(dif_minutos, 30)

if __name__ == '__main__':
    unittest.main()
