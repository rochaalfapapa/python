def calular_combustivel(km, km_l, valor_litro):
    valor_comb = km/km_l*valor_litro
    return valor_comb

def calculo_lucro(faturamento, despesas, valor_comb):
    lucro = faturamento-despesas-valor_comb-150
    #observe que para calcular o lucro subtraímos uma constante de 150 reais, ela é referente à uma constante (aproximada) dos custos de manutenção, seguro, IPVA, depreciação
    return lucro

def inserir_dados():
    km = float(input('Insira a quantidade de km rodados:'))
    km_l = float(input('Insira o consumo (km/l):'))
    valor_litro = float(input('Insira o valor por litro do combustível: R$'))
    return km, km_l, valor_litro

def inserir_despesas():
    str_despesas = input('Insira as despesas (separadas por vírgula): R$')
    despesas = 0.0 if not str_despesas else sum([float(valor.strip()) for valor in str_despesas.split(',')])
    return despesas

def inserir_faturamento():
    str_faturamento = input('Insira os faturamentos (separados por vírgula): R$')
    faturamento = 0.0 if not str_faturamento else sum([float(valor.strip()) for valor in str_faturamento.split(',')])
    return faturamento

def exibir_resultados(valor_comb, despesas, faturamento, lucro):
    print(f'O valor gasto com combustível foi de R${valor_comb:.2f}.')
    print(f'O valor total de despesas foi R${despesas:.2f}.')
    print(f'O faturamento foi de R${faturamento:.2f}.')
    print(f'O lucro líquido foi de R${lucro:.2f}.')


km, km_l, valor_litro = inserir_dados()
valor_comb = calular_combustivel(km, km_l, valor_litro)
despesas = inserir_despesas()
faturamento = inserir_faturamento()
lucro = calculo_lucro(faturamento, despesas, valor_comb)
exibir_resultados(valor_comb, despesas, faturamento, lucro)
