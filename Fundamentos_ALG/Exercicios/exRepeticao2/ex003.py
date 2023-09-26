'''Projete uma função que verifique se todos os elementos de uma lista de inteiros são menores
que 10.

1) Análise
    Projetar uma função que verifica se todos os elementos de uma lista de inteiros
    são menores que 10.

2) Definição dos tipos de dados
    A entrada da função será uma lista de inteiros, e a saída será booleeana
'''

# 3) Especificação
def todosMenorque10(numeros: int):
    '''Verifica se todos os elementos de uma lista de inteiros são menores que 10.

        Exemplos:
        >>> todosMenorque10([1, 2, 3, 4, 5, 6])
        True
        >>> todosMenorque10([]) is None
        True
        >>> todosMenorque10([60])
        False
    '''
    # 4) Implementação
    for i in numeros:
        if i >= 10:
            return False
        else:
            return True
    return None

# 5) Verificação
if __name__ == '__main__':
    import doctest
    doctest.testmod()

''' 6) Revisão'''
