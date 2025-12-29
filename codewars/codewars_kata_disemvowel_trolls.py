def disemvowel(string_):
    return ''.join([c for c in string_ if c not in 'AaEeIiOoUu'])

def disemvowel(string_):
    return string_.translate(str.maketrans('', '', 'aeiouAEIOU'))