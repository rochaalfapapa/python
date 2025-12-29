from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    contagem = Counter(word)
    return ''.join('(' if contagem[c] == 1 else ')' for c in word)