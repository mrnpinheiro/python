def harmonic_maior(n: int) -> float:
    '''
    Realiza o cálculo do número harmônico maior de ordem n, tal que:
    1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    O retorno esperado é um float com 2 casas decimais.
    '''
    num_h_maior = 0

    for h in range(1, n + 1):
        num_h_maior += 1/h

    return round(num_h_maior, 2)


def harmonic_menor(n: int) -> float:
    '''
    Realiza o cálculo do número harmônico menor de ordem n, tal que:
    1/n + 1/(n-1) + 1/(n-2) + ... + 1/2 + 1

    O retorno esperado é um float com 2 casas decimais.
    '''
    num_h_menor = 0

    for h in range(n, 0, -1):
        num_h_menor += 1/h

    return round(num_h_menor, 2)
