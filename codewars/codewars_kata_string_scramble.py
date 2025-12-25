def scramble(strng, array):
    resultado = [None] * len(strng)
    for caractere, posicao in zip(strng, array):
        resultado[posicao] = caractere
    return ''.join(resultado)