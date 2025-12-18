def count_sheeps(sheep):
    return sheep.count(True)

#2ª Opção de código, considerando um contexto em que seja interessante saber os itens verdadeiros de determinada condição, e não apenas a quantidade total de ocorrências positivas
def count_sheeps(sheep):
    ovelhas_presentes = [ovelha for ovelha in sheep if ovelha]
    return len(ovelhas_presentes)