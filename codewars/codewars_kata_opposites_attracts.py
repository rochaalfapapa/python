def lovefunc(flower1, flower2):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)


def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)


def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2