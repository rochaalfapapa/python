def get_count(sentence):
    total = 0
    for caractere in sentence:
        if caractere in 'aeiou':
            total += 1
    return total

def get_count(sentence):
    return sum(1 for char in sentence if char in 'aeiou')