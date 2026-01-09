def count_by(x: int, n: int) -> list:
    return [x * count for count in range(1, n + 1)]


#Solução mais clean

def count_by(x: int, n: int) -> list:
    return list(range(x, (x * n) + 1, x))