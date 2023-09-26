'''Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia
aparece na lista.

1) Análise
    Projetar uma função que conte quantas vezes o valor mínimo de uma
    lista de inteiros não vazia aparece na lista.
    
2) Levantamento dos tipos de dados
    A função receberá uma lista do tipo inteiro, e retornará a quantidade
    de vezes que o valor mínimo aparece em um valor inteiro. '''

def todosIguais(lista: list[int]) -> int:
    i: int = 0

    while i < (len(lista)-1):
        if lista[i] != lista[i + 1]:
            return False
        i = i + 1
    return True

# 3) Especificação
def qtdValorMinimo(lista: list[int]) -> int:
    '''Recebe uma lista do tipo inteiro e retorna a quantidade
        de vezes que o valor mínimo aparece em um valor inteiro.

        Exemplos:
        >>> qtdValorMinimo([1, 2, 1, 4, 1])
        3
        >>> qtdValorMinimo([4, 8, 12, 16])
        1
        >>> qtdValorMinimo([4, 2, 45, 1, 40, 1])
        2
        >>> qtdValorMinimo([]) is None
        True
    '''
    listaMenores: list[int] = []
    i: int = 1

    # 4) Implementação
    # Ex: lista = [4, 2, 45, 1, 40, 1]
    if len(lista) > 0:
        while todosIguais(lista) == False:
            while i < len(lista):
                if lista[0] < lista[i]:
                    listaMenores.append(lista[i])
                i = i + 1
            lista = listaMenores
            i = 1
        return len(lista)
    else:
        return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()