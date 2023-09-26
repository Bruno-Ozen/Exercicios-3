'''Projete uma função que crie uma nova lista somando 
um valor x especificado a cada elemento de uma lista de inteiros.

1) Análise
    Desenvolver uma função que cria uma nova lista somando um valor
x especificado a cada elemento de uma lista de inteiros.
2) Definição dos tipos de dados
    A entrada da função será uma variável inteira e uma lista de números inteiros, enquanto a
    saída também será, e do mesmo tamanho.'''

# 3) Especificação
def somaXemlista(valor: int, lista: int) -> list:
    '''Cria uma nova lista somando um valor x especificado a cada elemento de
    uma lista de inteiros.
    
    Exemplos:
    somaXemLista(4, [12, 93, 5000, 4])
    [16, 97, 5004, 8]
    somaXemLista(0, []) is None
    True'''
    listaSomada: int = []

    if len(lista) > 0:    
        for i in lista:
            listaSomada.append(i + valor)  
        return listaSomada
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod