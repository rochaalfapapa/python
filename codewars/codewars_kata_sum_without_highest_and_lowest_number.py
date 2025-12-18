def sum_array(arr):
    if arr is None or len(arr)<3:
        return 0
    arr_ordenado = sorted(arr)
    elementos_do_meio = arr_ordenado[1:-1]
    soma = sum(elementos_do_meio)
    return soma
