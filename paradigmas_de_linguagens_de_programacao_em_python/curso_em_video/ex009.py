while True:
    try:
        numero = eval(input('Digite um número para ver sua tabuada: '))
        break
    except Exception as e:
        print('Entrada inválida!\t', e)
print('-' * 16)
for i in range(1, 11):
    print(f'{numero:3} x {i:2} = {numero * i:3}')
print('-' * 16)
