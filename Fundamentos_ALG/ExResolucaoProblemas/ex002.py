''' 
Aluno: Bruno Henrique de Pinho
RA: 133301

EXERCÍCIO 2
1. Análise
	- Ler as idades de 4 pessoas, calcular e informar a média das
    idades
    - Ler as idades e retornar a idade da pessoa mais velha:
        - Calcular o maior entre os dois primeiros e dois ultimos
        números, e após isso compará-los e encontrar o maior.

2. Definição dos tipos de dados
	- Os dados serão definidos no tipo inteiro para a entrada das idades,
    e tipo decimal para a média delas. sendo representadas em anos.
'''

# 3. Especificação:
def mediaIdade(idade1, idade2, idade3, idade4: int):
    '''Lê as idades de 4 pessoas, calcula, e informa a média
        das idades.
        Exemplos:
        >>> mediaIdade(42, 45, 31, 60)
        44.5
        >>> mediaIdade(20, 15, 12, 18)
        16.25
    '''
    # 4. Implementação
    media = (idade1 + idade2 + idade3 + idade4)/4
    return media

def calculaMaior(n1, n2: int) -> int:
    '''Lê dois valores numéricos e retorna o maior deles
        Exemplos:
        >>> calculaMaior(1, 4)
        4
        >>> calculaMaior(12, 12)
        12
    '''
    if n1 > n2:
        return n1
    else:
        return n2

def maisVelha(idade1, idade2, idade3, idade4: int):
    '''Lê as idades de 4 pessoas, calcula, a idade da 
    pessoa mais velha.
        
        Exemplos:
        >>> maisVelha(80, 90, 42, 30)
        90
        >>> maisVelha(2, 10, 15, 11)
        15
    '''
    maior = calculaMaior(calculaMaior(idade1, idade2), calculaMaior(idade3, idade4))
    return maior

# 5. Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Foi necessária a implementação da função calculaMaior para otimizar
    o código e melhorar sua leitura, dividindo a função maisVelha.'''