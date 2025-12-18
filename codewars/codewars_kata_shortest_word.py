def find_short(s):
    lista = s.split()
    return min(len(palavra) for palavra in lista)