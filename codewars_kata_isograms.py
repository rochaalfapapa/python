def is_isogram(string):
    string_clean = string.lower()
    return len(string_clean) == len(set(string_clean))