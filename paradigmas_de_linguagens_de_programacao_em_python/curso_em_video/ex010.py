while True:
    try:
        saldo = float(input('Quanto dinheiro você tem na carteira? R$ ').replace(',', '.'))
        break
    except Exception as e:
        print('Entrada inválida!\t', e)
valor_dolar = 3.27
dolar = saldo / valor_dolar
print(f'Com R${saldo:.2f} você pode comprar US${dolar:.2f}')
