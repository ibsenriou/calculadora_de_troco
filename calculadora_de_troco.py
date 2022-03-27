from decimal import Decimal, ROUND_HALF_UP


def valor_a_ser_pago(valor):
    """Recebe um valor a ser pago e retorna o valor"""
    return valor


def valor_recebido(valor):
    return valor


def valor_de_troco_a_ser_devolvido(valor_total_da_compra, valor_pago):
    """Recebe o valor total da compra e o valor pago e retorna o troco"""
    if valor_total_da_compra > valor_pago:
        return 'O valor recebido não pode ser menor que o valor a ser pago'
    else:
        return valor_pago - valor_total_da_compra


def troco_a_devolver(valor_de_troco):
    """Recebe um valor de troco e retorna a menor quantidade de cédulas e moedas"""

    valor_de_troco = Decimal(str(valor_de_troco))
    cents = Decimal('.01')
    valor_de_troco = valor_de_troco.quantize(cents, ROUND_HALF_UP)

    cedulas = [
        100, 50, 10, 5, 1
    ]
    moedas = [
        Decimal('0.50'),
        Decimal('0.10'),
        Decimal('0.05'),
        Decimal('0.01'),
    ]
    cedulas_a_devolver = []
    moedas_a_devolver = []

    for cedula in cedulas:
        while valor_de_troco >= cedula:

            cedulas_a_devolver.append(cedula)

            valor_de_troco -= cedula

    for moeda in moedas:
        while valor_de_troco >= moeda:
            moedas_a_devolver.append(float(moeda))
            valor_de_troco -= moeda

    troco = [cedulas_a_devolver, moedas_a_devolver]
    return troco


def calculadora_de_troco(valor_total_da_compra, valor_pago):
    """Recebe o valor total da compra e o valor pago e retorna as cédulas e moedas à devolver"""
    troco = valor_de_troco_a_ser_devolvido(valor_total_da_compra, valor_pago)
    return troco_a_devolver(troco)
