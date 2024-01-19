from lista import ListaEstatica, Item

def inverteLista(lista: ListaEstatica) -> None:
    i: int = 0
    
    while i < lista.tamanho():
        aux = lista.ultimo()
        lista.remove()
        lista.inserePos(aux, i)
        i += 1
        
def main() -> None:
    lista = ListaEstatica(4)
    lista.insere(Item('1'))
    lista.insere(Item('2'))
    lista.insere(Item('3'))
    lista.insere(Item('4'))
    inverteLista(lista)
    lista.exibe()

if __name__ == '__main__':
    main()