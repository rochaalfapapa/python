def repeat_str(count: int, string: str) -> str:
    return count * string


#Solução de desafio do Gemini utilizando laço de repetição, sem utilização do "*"

def repeat_str(count: int, string: str) -> str:
    resultado = ''
    while count > 0:
        resultado += string
        count -= 1
    return resultado

#Solução utilizando o laço for

def repeat_str(count: int, string: str) -> str:
    resultado = []
    for _ in range(count):
        resultado.append(string)
    return ''.join(resultado)


#Solução laço for em linha única

def repeat_str(count: int, string: str) -> str:
    return ''.join(string for _ in range(count))