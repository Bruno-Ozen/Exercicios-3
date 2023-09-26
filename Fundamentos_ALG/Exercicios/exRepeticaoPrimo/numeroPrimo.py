def ePrimo(numero: int) -> bool:
    '''Calcula se um número é primo.
    
    Exemplos:
    >>> ePrimo(11)
    True
    >>> ePrimo(12)
    False
    >>> ePrimo(0)
    False
    '''

    i: int = 2
    resposta: bool = True
    
    if numero != 0:
        while i < numero and resposta == True:
            if numero % i == 0:
                resposta = False
            i = i + 1
        return resposta
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()