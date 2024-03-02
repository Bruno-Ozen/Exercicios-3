from lista import ListaEstatica, Item

'''
*Nota: Nesse exercício eu ia utilizar doctest, entretanto não consegui
localizar qual seria o formato em string da classe lista estática para
testar o doctest. Então tentei fazendo testes na prática no código.

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
    concatena_lista(ListaEstatica[0, 1, 2, 3], ListaEstatica[4, 5, 6, 7, 8])
    ListaEstatica[0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    concatena_lista(ListaEstatica[], ListaEstatica[])
    ListaEstatica[]
    '''
    
    if not l1.vazia() or not l2.vazia():
        l3: ListaEstatica = ListaEstatica(l1.tamanho() + l2.tamanho())
        if not l1.vazia():
            for i in range(l1.tamanho()):
                l3.insere(l1.buscaPos(i))
        if not l2.vazia():
            for i in range(l2.tamanho()):
                l3.insere(l2.buscaPos(i))
        return l3
    else:
        return ListaEstatica(0)
    
def main() -> None:
    l1 = ListaEstatica(4)
    l1.insere(Item('A'))
    l1.insere(Item('B'))
    l1.insere(Item('C'))
    l1.insere(Item('D'))
    print('Lista 1: ')
    l1.exibe()
    
    l2 = ListaEstatica(5)
    l2.insere(Item('V'))
    l2.insere(Item('W'))
    l2.insere(Item('X'))
    l2.insere(Item('Y'))
    l2.insere(Item('Z'))
    print('\nLista 2: ')
    l2.exibe()
    
    l3 = concatena_lista(l1, l2)
    print('\nLista 3: ')
    l3.exibe()
    
    # Fazendo a mesma operação com a função embutida:
    l3.esvazia()
    l3 = l1
    l4 = l3.concatena(l2)
    print('\nLista 3 concatenada com função embutida: ')
    l4.exibe()
    print('\nLista 3 invertida: ')
    l4.inverte()
    l4.exibe()
    
if __name__ == "__main__":
    main()