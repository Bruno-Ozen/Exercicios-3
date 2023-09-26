'''1. Projete uma função que verifique se todos os 
elementos de uma lista de booleanos são falsos'''

'''
    1) Análise
        Projetar uma função que verifica se todos os elementos
    de uma lista de booleanos são falsos.
    2) Definição dos tipos de dados
        O tipo de dados da entrada será uma lista do tipo booleano,
    e o retorno da função será 
'''

# 3) Especificação
def todosFalsos(lista: bool):
    '''
        Verifica se todos os elementos de uma lista de booleanos são falsos.

        Exemplos:
        >>> todosFalsos([False, False, False])
        True
        >>> todosFalsos([True, False])
        False
        >>> todosFalsos([])
        False
    '''
    # 4) Implementação
    resp = True
    if len(lista) > 0:
        for i in lista:
            if i == True:
                resp = False
        return resp
    return False

# 5) Verificação
if __name__ == '__main__':
    import doctest
    doctest.testmod()

''' 6) Revisão:
    Nenhuma alteração foi necessária.'''