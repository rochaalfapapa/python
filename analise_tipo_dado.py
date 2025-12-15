def analisar_tipo(dado):
    return f'{dado} é numérico' if isinstance(dado, (int, float, complex)) else f'{dado} é uma sequencia' if isinstance(dado, (str, list, tuple)) else 'Tipo desconhecido'
