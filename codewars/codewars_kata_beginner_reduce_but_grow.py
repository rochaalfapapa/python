def grow(arr):
    resultado = 1
    for x in arr:
        resultado *= x
    return resultado

import math

def grow(arr):
    return math.prod(arr)


#desafio Gemini

import math

def grow(arr):
    if any(x == 0 for x in arr):
        return 0
    if any(x % 2 != 0 for x in arr):
        return math.prod(x for x in arr if x % 2 != 0)
    return 0

def grow(arr):
    result = 1
    is_odd = False

    for x in arr:
        if x == 0:
            return 0
        if x % 2 != 0:
            result *= x
            is_odd = True
    return result if is_odd else 0