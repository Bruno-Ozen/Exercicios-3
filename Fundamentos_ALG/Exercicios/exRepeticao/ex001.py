'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Projetar uma função que encontre o índice 
    (posição) da primeira ocorrência do valor máximo 
    em uma lista não vazia.

2) Definição dos tipos de dados
    - A entrada da função de encontrar o índice do valor máximo
    será uma lista, e a sua saída, o index, será representado pelo
    tipo inteiro;
    - Caso a lista seja vazia, retorna None;
    - Haverá uma variável para o índice do valor máximo, que será do
    tipo inteiro, assim como as variáveis de índice (i e j) do "scan"
    do while.
'''

# 3) Especificação
def findIndexfromMax(numeros: int) -> int:
    '''Compara cada termo com todos os outros restantes, incluindo ele mesmo.
    Se o termo a ser comparado (index i) for menor que o próximo (index j), então
    passa a comparar o próximo termo com todos os outros restantes. Se
    o termo do index i for maior que o do index max, então index max recebe i (o do
    maior item encontrado até então. Se todos os termos forem iguais, então retorna
    o primeiro index (0).

    Exemplos:
    >>> findIndexfromMax([1, 2, 3])
    2
    >>> findIndexfromMax([0])
    0
    >>> findIndexfromMax([]) is None
    True
    >>> findIndexfromMax([2, 2, 2, 2, 2, 2])
    0
    >>> findIndexfromMax([4, 5, 2, 3, 1])
    1
    '''
    # 4) Implementação
    max: int = 0
    i: int = 0
    j: int = 0
    if len(numeros) > 0:
        while i < len(numeros):
            while j < len(numeros):
                if numeros[i] < numeros[j]:
                    break
                elif numeros[i] > numeros[max]:
                    max = i
                j = j + 1
            i = i + 1
        return max
    else:
        return None

# 5) Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Tive que pesquisar como verificar no doctest o retorno de None.
    Descobri que a única forma de verificar é colocando "Is None" depois
    da chamada do método.
'''
