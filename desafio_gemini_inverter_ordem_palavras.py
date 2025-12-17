def inverter_ordem_palavras(frase):
    palavras = frase.split()
    frase_invertida = palavras[::-1]
    return " ".join(frase_invertida)