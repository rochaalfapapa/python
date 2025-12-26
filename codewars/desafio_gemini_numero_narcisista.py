def numero_narcisista(num):
    quantidade = len(str(num))
    soma = sum(int(x) ** quantidade for x in str(num))
    return soma == num