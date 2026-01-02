def update_light(current):
    current_clean = current.lower()
    return 'yellow' if current_clean == 'green' else 'red' if current_clean == 'yellow' else 'green'

#Solução utilizando dicionários

def update_light(current):
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]