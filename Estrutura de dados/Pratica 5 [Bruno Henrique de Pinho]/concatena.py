from lista import ListaEstatica, Item

'''
1) Análise
    Dadas duas listas, escrever uma função que retorne uma terceira 
lista que corresponde à concatenação das listas de entrada.

2) Definição dos tipos de dados
    A função terá como entrada duas listas do tipo ListaEstatica, e retornará
uma terceira lista do mesmo tipo.
'''

# 3) Especificação
def concatena_lista(l1: ListaEstatica, l2: ListaEstatica) -> ListaEstatica:
    ''' Dadas duas listas, retorna uma terceira lista que corresponde
        à concatenação das listas de entrada.
        
    Exemplos:
    >>> concatena_lista()
    '''
    
    if not l1.vazia or not l2.vazia:
        l3: ListaEstatica = ListaEstatica(l1.tamanho() + l2.tamanho())
        if not l1.vazia():
            for i in range(l1.tamanho):
                l3.insere(l1.buscaPos(i))
        if not l2.vazia():
            for i in range(l2.tamanho):
                l3.insere(l2.buscaPos(i))
        return l3
    else:
        return ListaEstatica(0)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()