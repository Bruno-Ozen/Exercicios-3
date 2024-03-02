from arvores import *

def main() -> None:
    a = ABB()
    a.insere(Item(4))
    a.insere(Item(2))
    a.insere(Item(3))
    a.insere(Item(1))
    a.insere(Item(6))
    a.insere(Item(5))
    a.insere(Item(7))
    a.exibe()

    no = a.busca(Item(7))
    if no != None:
        print(no.elemento)
    else: 
        print(no)

    print('Altura da ABB a =', a.altura())
    print('Percurso da ABB a em in-ordem:')
    a.percorreArvore(1)

    print(a.string())

    a.remove(Item(7))
    a.exibe()
    a.remove(Item(4))
    a.exibe()

main()