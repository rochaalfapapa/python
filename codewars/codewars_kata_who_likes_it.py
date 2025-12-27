def likes(names):
    quantidade = len(names)
    if quantidade == 0:
        return 'no one likes this'
    elif quantidade == 1:
        return f'{names[0]} likes this'
    elif quantidade == 2:
        return f'{names[0]} and {names[1]} like this'
    elif quantidade == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {quantidade-2} others like this'
    

def likes(names):
    match names:
        case[]:
            return 'no one likes this'
        case [name1]:
            return f'{name1} likes this'
        case [name1, name2]:
            return f'{name1} and {name2} like this'
        case [name1, name2, name3]:
            return f'{name1}, {name2} and {name3} like this'
        case [name1, name2, name3, *others]:
            return f'{name1}, {name2} and {len(names) - 2} others like this'