def clean_string(s):
    pile = []

    for c in s:
        if c == '#':
            if pile:
                pile.pop()
        else:
            pile.append(c)
            
    return ''.join(pile)