def high_and_low(numbers):
    lista_int = [int(x) for x in numbers.split()]
    return f"{max(lista_int)} {min(lista_int)}"