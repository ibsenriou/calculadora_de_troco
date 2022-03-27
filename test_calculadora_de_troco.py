from calculadora_de_troco import *


class CalculadoraDeTroco(unittest.TestCase):
    def test_valor_a_ser_pago_quando_1(self):
        self.assertEqual(valor_a_ser_pago(1), 1)

    def test_valor_a_ser_pago_quando_10(self):
        self.assertEqual(valor_a_ser_pago(10), 10)

    def test_valor_recebido_quando_5(self):
        self.assertEqual(valor_recebido(5), 5)

    def test_valor_recebido_quando_100(self):
        self.assertEqual(valor_recebido(100), 100)

    def test_valor_de_troco_a_ser_devolvido_quando_valor_da_compra_for_12_e_valor_pago_for_20(self):
        self.assertEqual(valor_de_troco_a_ser_devolvido(12, 20), 8)

    def test_valor_de_troco_a_ser_devolvido_quando_valor_da_compra_for_1500_e_valor_pago_for_2000(self):
        self.assertEqual(valor_de_troco_a_ser_devolvido(1500, 2000), 500)

    def test_valor_de_troco_a_ser_devolvido_quando_valor_da_compra_for_maior_que__o_valor_pago_for_2000(self):
        self.assertEqual(valor_de_troco_a_ser_devolvido(3, 1),
                         'O valor recebido não pode ser menor que o valor a ser pago')

    def test_funcao_troco_a_devolver_quando_troco_for_2(self):
        self.assertEqual(troco_a_devolver(2), [[1, 1], []])

    def test_funcao_troco_a_devolver_quando_troco_for_50_centavos(self):
        self.assertEqual(troco_a_devolver(0.50), [[], [0.50]])

    def test_funcao_troco_a_devolver_quando_troco_for_13_reais_e_61_centavos(self):
        self.assertEqual(troco_a_devolver(13.61), [[10, 1, 1, 1], [0.50, 0.10, 0.01]])

    def test_calculadora_de_troco_quando_valor_da_compra_for_99_e_valor_pago_for_100(self):
        self.assertEqual(calculadora_de_troco(99, 100), [[1], []])

    def test_calculadora_de_troco_quando_valor_da_compra_for_196_reais_e_45_e_valor_pago_for_200(self):
        self.assertEqual(calculadora_de_troco(196.45, 200), [[1, 1, 1], [0.50, 0.05]])