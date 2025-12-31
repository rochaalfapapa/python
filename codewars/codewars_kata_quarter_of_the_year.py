def quarter_of(month):
    return (month + 2) // 3


#Solução utilizando lista
def quarter_of(month):
    quarters = [None, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
    return quarters[month]