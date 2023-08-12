'''
Aluno: Bruno Henrique de Pinho
RA: 133301

EXERCÍCIO 3
1. Análise
	- Receber 3 valores reais, verificar se os valores podem
    ser os lados de um triângulo verificando em cada um dos valores
    se o mesmo é menor que a soma dos dois adjacentes; se sim, retornar
    verdadeiro. Se não, retornar falso;
    - Receber 3 valores sendo esses os lados de um triângulo. Se os valores
    formarem um triângulo, então verificar o seu tipo, sendo equilátero se 
    os três lados forem iguais, isósceles se dois lados forem iguais e um diferente, 
    e escaleno se os três lados forem diferentes, retornando o tipo de triângulo que 
    os 3 valores formam.

2. Definição dos tipos de dados
	- Os tipos de dados serão representados em números reais para as entradas 
    dos lados do triângulo, e booleano para o retorno após a verificação;
    - Na função de tipo do triângulo as entradas serão representadas igualmente
    por números reais, entretanto sua saída será do tipo caractere, informando
    o tipo do triângulo.
'''

# 3.0. Especificação:
def eTriangulo(a, b, c: float) -> bool:
    '''Lê os três valores e verifica se formam um triângulo.

        Exemplos:
        >>> eTriangulo(2, 42, 1)
        False
        >>> eTriangulo(4, 4, 4)
        True
        >>> eTriangulo(1.5, 2.5, 1.5)
        True
        >>> eTriangulo(43, 43.1, 11)
        True
    '''
    # 4. Implementação
    return a < (b + c) and b < (a + c) and c < (a + c)

# 3.1 Especificação:
def tipoTriangulo(a, b, c: float) -> str:
    '''Se os valores formarem um triângulo, a função
    lê os seus três lados, verifica o tipos e faz o 
    seu retorno.

        Exemplos:
        >>> tipoTriangulo(2222, 1, 2)
        'Valores inválidos.'
        >>> tipoTriangulo(1, 1, 1)
        'Equilátero'
        >>> tipoTriangulo(12, 10, 12)
        'Isósceles'
        >>> tipoTriangulo(14, 13, 11)
        'Escaleno'
    '''
    # 4. Implementação
    if eTriangulo(a, b, c):
        if a == b and b == c:
            return 'Equilátero'
        elif a == b or b == c or a == c:
            return 'Isósceles'
        else:
            return 'Escaleno'
    else:
        return 'Valores inválidos.'

# 5. Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Notei que eu esqueci de colocar o parenteses para chamar
    a função é triângulo dentro da função tipo triângulo.'''