'''1) Análise
        Fazer uma função que recebe uma lista de caracteres e mais dois caracteres, C1 e C2.
    Criar uma nova lista trocando todas as ocorrências de C1 por C2.

    2) Definição dos tipos de dados
        A função terá como entrada 3 parâmetros: Uma lista de caracteres e duas variáveis do tipo caractere.
    A saída da função será uma lista de caracteres.
    '''

# 3) Especificação
def trocaCaractere(lista: list[str], c1: str, c2: str) -> list[str]:
    '''Recebe uma lista de caracteres e mais dois caracteres, C1 e C2, e
    cria uma nova lista trocando todas as ocorrências de C1 por C2.
    
    Exemplos:
    >>> trocaCaractere(['A', 'B', 'A', 'B'], 'A', 'B')
    ['B', 'B', 'B', 'B']
    >>> trocaCaractere(['J', 'j', 'k'], 'j', '')
    ['J', '', 'k']
    >>> trocaCaractere([], 'A', 'B') is None
    True
    >>> trocaCaractere(['B', 'b', 'k'], 'F', 'J')
    ['B', 'b', 'k']
    '''
    listaTrocada: list[str] = []
    if len(lista) > 0:
        for i in range(len(lista)):
            if lista[i] == c1:
                listaTrocada.append(c2)
            else:
                listaTrocada.append(lista[i])
        return listaTrocada
    else:
        return None

# 5) Verificação
if __name__ == '__main__':
    import doctest
    doctest.testmod()

''' 6) Revisão

'''