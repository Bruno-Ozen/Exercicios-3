'''
    Projete uma função que verifique se a quantidade de elementos
    de uma lista de floats é menor que 4.
'''

def sizeMinorthan4(lista: list) -> int:
    '''Retorna se uma lista de floats é menor que 4. Se a lista for vazia, retorna True.

        Exemplos:
        >>> sizeMinorthan4([2, 4])
        True
        >>> sizeMinorthan4([2, 1, 2, 2])
        False
        >>> sizeMinorthan4([])
        True
    '''

    tamanho: int = 0
    for i in lista:
        tamanho = tamanho + 1
    return tamanho < 4

if __name__ == '__main__':
    import doctest
    doctest.testmod()