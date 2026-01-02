def digitize(n):
    return [int(x) for x in str(n)][::-1]


#solução mais indicada (de acordo com o codewars)

def digitize(n):
    return [int(x) for x in str(n)[::-1]]