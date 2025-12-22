def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    movimentos = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}
    x, y = 0, 0

    for passo in walk:
        dx, dy = movimentos[passo]
        x, y = x + dx, y + dy
    return x == 0 and y == 0