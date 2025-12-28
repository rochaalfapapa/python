def xo(s):
    quantidade_x = sum(1 for c in s.lower() if c in 'x')
    quantidade_o = sum(1 for c in s.lower() if c in 'o')
    return quantidade_x == quantidade_o

def xo(s):
    texto_minusculo = s.lower()
    return texto_minusculo.count('x') == texto_minusculo.count('o')

from collections import Counter

def xo(s):
    from collections import Counter
    contagem = Counter(s.lower())
    return contagem['x'] == contagem['o']