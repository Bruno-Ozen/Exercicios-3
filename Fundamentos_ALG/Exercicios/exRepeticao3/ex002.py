'''
O ALGORITMO ABAIXO ESTÁ INCORRETO POIS ELE CRIA UMA LISTA DENTRO DA OUTRA, ENQUANTO
O EXERCÍCIO PEDE PARA FAZER UMA LISTA SÓ SEM SUBLISTAS
    1) Análise
        Projetar uma função que receba como entrada uma lista lst de números e cria uma nova lista
    colocando os valores negativos de lst antes dos positivos.
    2) Definição dos tipos de dados
        A entrada da função será uma lista de números inteiros nomeada lst, e a saída também
    será uma lista do tipo inteiro. A função também contará com uma lista do tipo inteiro para
    armazenar os números positivos e posteriormente juntá-la com a lista ordenada.
'''

# 3) Especificação
def ordenaNegativos(lst: list[int]) -> list[int]:
    '''Recebe como entrada uma lista lst de números e cria uma nova lista
    colocando os valores negativos de lst antes dos positivos.

    Exemplos:
    >>> ordenaNegativos([1, 4, -3, 1, -2])
    [-3, -2, 1, 4, 1]
    >>> ordenaNegativos([-2, 4, -2, 4, -2, 4])
    [-2, -2, -2, 4, 4, 4]
    >>> ordenaNegativos([-4, - 4,-5, -6, -2])
    [-4, - 4,-5, -6, -2]
    >>> ordenaNegativos([])
    []
    '''

    # 4) Implementação
    listaOrdenada: list[int] = []
    listaPositivos: list[int] = []

    for i in range(len(lst)):
        if lst[i] < 0:
            listaOrdenada.append(lst[i])
        else:
            listaPositivos.append(lst[i])
    listaOrdenada.append(listaPositivos)
    return listaOrdenada

# 5) Verificação
if __name__ == '__main__':
    import doctest
    doctest.testmod()

''' 6) Revisão

'''