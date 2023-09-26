'''1) Análise
        Fazer uma função que calcule o valor de H a partir de n, sendo
    H = 1 + 1/2 + 1/3 + ... + 1/n.

    2) Definição dos tipos de dados
        A entrada da função se dará por um número inteiro n. Já a saída
    será um valor real, denominado H. A função também contará com uma variável
    inteira para o denominador da fração, que será incrementada até o valor de n.'''

# 3) Especificação
def somatorioFracao(n: int) -> float:
    '''Calcula o valor de H a partir de n, sendo
    H = 1 + 1/2 + 1/3 + ... + 1/n.

    Exemplos:
    >>> somatorioFracao(3)
    1,8333333333333333333333333333333
    >>> somatorioFracao(0)
    0
    >>> somatorioFracao(4)
    2,0833333333333333333333333333333
    >>> somatorioFracao(-2)
    0
    >>> somatorioFracao(0)
    0
    '''
    denominador: int = 1
    somatorio: int = 0

    if n > 0:
        while denominador <= n:
            somatorio = somatorio + 1/denominador
            denominador = denominador + 1
        return somatorio
    else:
        return 0 

if __name__ == '__main__':
    import doctest
    doctest.testmod()