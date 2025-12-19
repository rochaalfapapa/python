def reverse_words(text):
    lista = text.split(' ')
    lista_invertida = [palavra[::-1] for palavra in lista]
    return ' '.join(lista_invertida)

def reverse_words(text):
    return ' '.join(palavra[::-1] for palavra in text.split(' '))