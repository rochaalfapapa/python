def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_triangle(a, b, c):
    s = sorted([a, b, c])
    return s[0] + s[1] > s[2]