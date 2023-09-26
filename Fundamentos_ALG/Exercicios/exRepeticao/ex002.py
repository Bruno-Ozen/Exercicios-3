'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Projetar uma função que verifica se uma lista de valores está em ordem não decrescente;
    - Caso a lista esteja em qualquer ordem que não seja decrescente, retorna verdadeiro. Caso
    seja decrescente, então retorna falso;
    - Se todos os itens forem iguais, então retorna verdadeiro;
    - Se a lista for vazia, também retorna verdadeiro.

2) Definição dos tipos de dados
    - O valor de entrada da função isNotDecrescent() será uma lista de números
    do tipo inteiro, enquanto o valor de saída será booleano (True or False);
    - Haverá uma variável para o index que percorrerá a lista de numeros no while.
'''

# 3) Especificação
def isNotDecrescent(numeros: int) -> bool:
    '''Verifica se uma lista de valores está em ordem não decrescente. Se
        todos os valores da lista forem iguais, então retorna True. Caso
        a lista seja vazia, também retorna True. O código verifica primeiro
        se a lista é vazia, se for, então retorna True. Se a lista conter
        elementos, então a função compara de dois em dois termos até o último,
        fazendo as seguintes ações para as respectivas condições:
            1. Se o primeiro termo, em algum ponto da lista for menor que o segundo termo, então
            é lógico pensar que a lista é crescente e portanto, não descrescente, ou se o termo anterior
            for igual ao próximo, a função considera como não decrescente. Porém, se em algum ponto da lista
            as primeiras duas condições não forem encontradas, então retorna falso (no caso do termo anterior
            ser maior do que o próximo, e logo, decrescente).
    
        Exemplos:
        >>> isNotDecrescent([9, 8, 7, 6])
        False
        >>> isNotDecrescent([9, 8, 2])
        False
        >>> isNotDecrescent([1, 2, 3, 4])
        True
        >>> isNotDecrescent([1, 1, 1])
        True
        >>> isNotDecrescent([])
        True
    '''
    # 4) Implementação
    index: int = 0
    naoeDecrescente: bool = True

    if len(numeros) > 0:
        while index < (len(numeros) - 1) and naoeDecrescente == True:
            if numeros[index] > numeros[index + 1]:
                naoeDecrescente = False
            index = index + 1
            
    return naoeDecrescente

# 5) Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Nenhuma alteração foi necessária. Só tenho a dizer que o primeiro
    exercício deu uma boa base para esse.
'''
