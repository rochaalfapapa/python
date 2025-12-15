def cookie(x):
    #name = 'Zach' if isinstance(x, str) else 'Monica' if isinstance(x,int) or isinstance(x, float) else 'the dog'
    #Zach str
    #Monica float or int
    #the dog
    #"Who ate the last cookie? It was {name}!"
    if isinstance(x, str):
        name = 'Zach'
    elif isinstance(x, (int, float)):
        name = 'Monica'
    else:
        name = 'the dog'
    return f'Who ate the last cookie? It was {name}!'