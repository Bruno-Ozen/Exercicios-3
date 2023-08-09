''' EXERCÍCIO 2
1. Análise
	-  Ler as idades de 4 pessoas, calcular e informar a média das
    idades e a idade da mais velha.

2. Definição dos tipos de dados
	- Os dados serão definidos no tipo inteiro para a entrada das idades,
    e tipo decimal para a média delas. sendo representadas em anos.
'''

# 3. Especificação:
def mediaIdade(idade1, idade2, idade3, idade4: int):
    '''Lê as idades de 4 pessoas, calcula, e informa a média
        das idades e a idade da mais velha.
        
        Exemplos:
        >>> mediaIdade(42, 45, 31, 60)
        [44.5, 60]
        >>> mediaIdade(20, 15, 12, 18)
        [16.25, 20]
    '''
    # 4. Implementação
    media = (idade1 + idade2 + idade3 + idade4)/4
    maisVelha: int = 0
    if idade1 > idade2:
        maisVelha = idade1
    elif idade3 > idade4:
        maisVelha = idade3
    elif idade2 > idade4:
        maisVelha = idade2
    else:
        maisVelha = idade4
    return [media, maisVelha]

# 5. Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Nenhuma modificação foi necessária.'''