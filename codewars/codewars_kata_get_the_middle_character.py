def get_middle(s):
    tamanho = len(s)
    meio = tamanho // 2
    if tamanho % 2 != 0:
        return s[meio]
    else:
        return s[meio - 1:meio + 1]

def get_middle(s):
    m = len(s) // 2
    return s[m] if len(s) % 2 != 0 else s[m-1:m+1]