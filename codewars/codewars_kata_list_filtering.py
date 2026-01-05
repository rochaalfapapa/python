def filter_list(l):
    return [x for x in l if isinstance(x, int)]

#Solução utilizando filter() e lambda

def filter_list(l):
    return list(filter(lambda x: isinstance(x, int), l))