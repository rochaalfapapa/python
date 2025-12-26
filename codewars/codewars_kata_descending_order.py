def descending_order(num):
    lista_ordenada = sorted(str(num), reverse=True)
    return int(''.join(lista_ordenada))