def longest(a1: str, a2: str) -> str:
    return ''.join(sorted(set(a1) | set(a2)))