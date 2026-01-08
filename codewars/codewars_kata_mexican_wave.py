def wave(people: str) -> list:
    list_words = []
    for w in range(len(people)):
        if people[w] != ' ':
            list_words.append(people[:w] + people[w].upper() + people[w + 1:])
    return list_words

#Solução com List Comprehension

def wave(people: str) -> list:
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i] != ' ']