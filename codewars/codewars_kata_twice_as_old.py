def twice_as_old(dad_years_old: int, son_years_old: int) -> int:
    return abs(dad_years_old - (2 * son_years_old))


#Solução implementando validação dos dados antes do cálculo
def twice_as_old(dad_years_old: int, son_years_old: int) -> int:
    if dad_years_old < 0 or son_years_old < 0:
        raise ValueError('As idades não podem ser negativas.')
    if (dad_years_old - son_years_old) < 18:
        raise ValueError('Idade do pai inconsistente com a do filho.')
    return abs(dad_years_old - (2 * son_years_old))

#Utilizando o bloco try/except
try:
    resultado = twice_as_old(25, 20)
    print(f'Resultado: {resultado}')
except ValueError as e:
    print(f'Erro de validação: {e}')