"""
def get_sum(a,b):
    lista = (a, b)
    lista_ordenada = sorted(lista)
    soma = 0
    for x in range(lista_ordenada[0],lista_ordenada[1]+1):
        soma += x
    return soma
"""

"""
def get_sum(a,b):
    lista = (a,b)
    soma = 0
    for x in range(min(lista),max(lista)+1):
        soma += x
    return soma
"""

"""
def get_sum(a,b):
    lista = (a,b)
    total = sum(range(min(lista), max(lista)+1))
    return total
"""

def get_sum(a,b):
    return ((abs(a-b)+1)*(a+b))//2