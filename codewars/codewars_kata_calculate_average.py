def find_average(numbers):
    return sum(numbers)/len(numbers) if numbers else 0


#Resolvendo de outra forma, fazendo o tratamento de exceção
def find_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0