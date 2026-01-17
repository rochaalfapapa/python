def abbrev_name(name: str) -> str:
    list_name = name.split()
    initial = []
    for x in list_name:
        initial.append(x[0].upper())
    return '.'.join(initial)


#Solução de linha única

def abbrev_name(name: str) -> str:
    return '.'.join(word[0].upper() for word in name.split())