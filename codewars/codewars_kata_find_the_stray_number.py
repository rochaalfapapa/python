def stray(arr: list) -> int:
    result = 0
    for i in arr:
        result ^= i
    return result


#Solução alternativa
from functools import reduce
from operator import xor

def stray(arr: list) -> int:
    return reduce(xor, arr)