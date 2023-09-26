'''
    1) Análise
        Projetar uma função que cria uma nova lista removendo todos os valores nulos de uma lista de
    inteiros.
    2) Definição dos tipos de dados
        A entrada da função será uma lista de números inteiros, enquanto a saída será uma nova lista, também
    inteiros.
'''

# 3) Especificação
def removeNulos(lista: list[int]) -> list[int]:
    '''Cria uma nova lista removendo todos os valores nulos de uma lista de inteiros.

        Exemplos:
        >>> removeNulos([2, 0, 1, 0, 0, 0])
        [2, 1]
        >>> removeNulos([0, 0, 0, 0])
        []
        >>> removeNulos([])
        []
    '''

    # 4) Implementação
    listaSemNulos: list[int] = []

    if len(lista) > 0:
        for i in range(len(lista)):
            if lista[i] != 0:
                listaSemNulos.append(lista[i])
    return listaSemNulos

# 5) Verificação
if __name__ == '__main__':
    import doctest
    doctest.testmod()

''' 6) Revisão

'''