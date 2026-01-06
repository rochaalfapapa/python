def tower_builder(n_floors):
    return [('*' * (2 * i + 1)).center((2 * n_floors) - 1) for i in range(n_floors)]