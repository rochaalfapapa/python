def accum(st):
    resultado = []
    for i, letra in enumerate(st):
        lista = (letra * (i + 1))
        resultado.append(lista.capitalize())
    return '-'.join(resultado)

def accum(st):
    return '-'.join((letra * (i + 1)).capitalize() for i, letra in enumerate(st))