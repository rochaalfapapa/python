def open_or_senior(data):
    resultado = []

    for idade, handicap in data:
        if idade >= 55 and handicap > 7:
            resultado.append('Senior')
        else:
            resultado.append('Open')
    
    return resultado


def open_or_senior(data):
    return ['Senior' if (idade >= 55 and handicap > 7) else 'Open' for idade, handicap in data]