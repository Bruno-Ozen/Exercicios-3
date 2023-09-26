'''
    Usando while, faça uma função que retorne se um elemento está em uma lista.
'''

def tamanhoLista(lista: list) -> int:
    '''Retorna o tamanho de uma lista. Se a lista for vazia, então retorna 0

        Exemplos:
        >>> tamanhoLista([2, 3, 4, 1, 2])
        5
        >>> tamanhoLista([])
        0
        >>> tamanhoLista([2])
        1
    '''
    tamanho: int = 0
    for i in lista:
        tamanho = tamanho + 1
    return tamanho

def estanaLista(elemento, lista: list) -> bool:
    '''Retorna se um elemento está em uma lista. Se a lista for vazia, então retorna False.

        Exemplos:
        >>> estanaLista(1, [1, 2, 3, 4, 5, 6])
        True
        >>> estanaLista('Perenaldo', ['Ronaldo', 'Josealdo'])
        False
        >>> estanaLista(5.2, [])
        False
    '''
    i: int = 0
    if tamanhoLista(lista) > 0:
        while i < tamanhoLista(lista):
            if lista[i] == elemento:
                return True
            i = i + 1
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()