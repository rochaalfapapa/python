def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            return value1 / value2
        
#resolução utilizando dicionário de funções
import operator

def basic_op(op, value1, value2):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    return ops[op](value1, value2)