def sort_array(source_array):
    impares = iter(sorted([n for n in source_array if n % 2 != 0]))
    return [n if n % 2 == 0 else next(impares) for n in source_array]