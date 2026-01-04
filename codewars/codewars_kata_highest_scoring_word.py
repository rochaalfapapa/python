def high(x):
    list_words = x.split()
    list_score = [sum((ord(char) - ord('a') + 1) for char in word) for word in list_words]
    return list_words[list_score.index(max(list_score))]


#Higher-Order-Functions
#Solução utilizando função com o parâmetro key
def high(x):
    return max(x.split(), key = lambda word: sum(ord(c) - ord('a') + 1 for c in word))