def find_uniq(arr: list):
    s = set(arr)
    elements = list(s)
    if arr.count(elements[0]) == 1:
        return elements[0]
    else:
        return elements[1]
    

#Solução utilizando o Counter
from collections import Counter
def find_uniq(arr: list):
    return Counter(arr).most_common()[-1][0]