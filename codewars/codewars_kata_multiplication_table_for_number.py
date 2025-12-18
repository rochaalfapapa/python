def multi_table(number):
    lista = []
    for i in range(1,11):
        linha = f"{i} * {number} = {i*number}"
        lista.append(linha)
    resultado_final = "\n".join(lista)
    return resultado_final