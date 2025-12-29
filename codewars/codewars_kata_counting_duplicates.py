def duplicate_count(text):
    contagem = 0
    texto_minusculo = text.lower()
    for c in set(texto_minusculo):
        if texto_minusculo.count(c) > 1:
            contagem += 1
    return contagem

def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])

#Solução mais performática
from collections import Counter

def duplicate_count(text):
    contagem = Counter(text.lower())
    return sum(1 for v in contagem.values() if v > 1)