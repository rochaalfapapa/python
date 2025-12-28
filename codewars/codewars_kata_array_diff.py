def array_diff(a, b):
    b_set = set(b)
    return [x for x in a if x not in b_set]


def array_equal(a, b):
    b_set = set(b)
    return [x for x in a if x in b_set]