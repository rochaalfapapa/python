def remove_char(s):
    return ''.join(char for index, char in enumerate(s) if index > 0 and index < len(s) - 1)


#resolução mais simples

def remove_char(s):
    return s[1 : -1]