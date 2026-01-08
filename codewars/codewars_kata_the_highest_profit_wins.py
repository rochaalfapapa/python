def min_max(lst: list) -> list:
    return [min(lst), max(lst)]


#Solução utilizando o NumPy, visando performace em grandes dados

import numpy as np

def min_max_numpy(lst: list) -> list:
    arr = np.array(lst)
    return [arr.min().item(), arr.max().item()]