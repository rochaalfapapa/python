def order(sentence):
    lista_ordenada = sorted(sentence.split(), key = extrair_numero)

    return ' '.join(lista_ordenada)

def extrair_numero(palavra):
    for caractere in palavra:
        if caractere.isdigit():
            return int(caractere)
        
#Utilizando lambda

def order(sentence):
    lista_ordenada = sorted(sentence.split(), key = lambda palavra: min(c for c in palavra if c.isdigit()))
    return ' '.join(lista_ordenada)