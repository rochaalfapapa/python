def to_jaden_case(string: str) -> str:
    return ' '.join(word.capitalize() for word in string.split())