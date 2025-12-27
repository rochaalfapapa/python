def is_cube(n):
    cube_root = round(abs(n) ** (1/3)) * (1 if n >=0 else -1)
    return cube_root ** 3 == n

def filter_cubes(numeros):
    return list(filter(is_cube, numeros))

def get_cubes(numeros):
    return (n for n in numeros if is_cube(n))

def teste():
    my_numbers = [1, 2, 8, 27, 64]
    result = get_cubes(my_numbers)
    print(result)