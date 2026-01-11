def cup_and_balls(b: int, arr: list) -> int:
    for cup_a, cup_b in arr:
        if cup_a == b:
            b = cup_b
        elif cup_b == b:
            b = cup_a
    return b

#Solução mais "robusta", com tratamento de erro e Type Hinting

from typing import List, Tuple
import logging

logging.basicConfig(
    filename = 'app_error.log',
    filemode = 'w',
    level = logging.ERROR,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%d/%m/%Y %H:%M:%S'
)

def cup_and_balls(b: int, arr: List[List[int]]) -> int:
    try:
        for cup_a, cup_b in arr:
            if cup_a == b:
                b = cup_b
            elif cup_b == b:
                b = cup_a
        return b
    except ValueError as e:
        logging.error(f'Erro de desempacotamento: {e}. Entrada inválida encontrada.')
        return b
    
#Solução com uma Assertion
def cup_and_balls(b: int, arr: list) -> int:
    assert all(len(swap) == 2 for swap in arr)
    for cup_a, cup_b in arr:
        if cup_a == b:
            b = cup_b
        elif cup_b == b:
            b = cup_a
    return b

#Solução mais completa e robusta
from typing import List
import logging

logging.basicConfig(
    filename = 'app_error.log',
    filemode = 'w',
    level = logging.ERROR,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%d/%m/%Y %H:%M:%S'
)

def cup_and_balls(b: int, arr: List[List[int]]) -> int:
    try:
        for cup_a, cup_b in arr:
            if cup_a == b:
                b = cup_b
            elif cup_b == b:
                b = cup_a
        return b
    except ValueError:
        logging.exception('Erro crítico de desempacotamento no array de trocas.')
        return b