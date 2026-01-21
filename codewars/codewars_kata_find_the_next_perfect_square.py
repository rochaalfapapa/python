from math import sqrt
def find_next_square(sq: int) -> int:
    if (root := sqrt(sq)).is_integer():
        return int((root + 1) ** 2)
    else:
        return -1