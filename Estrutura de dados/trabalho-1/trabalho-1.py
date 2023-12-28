'''
2) Definição dos tipos de dados
    - Os clientes serão representados por uma classe Cliente, que poderá ser preferencial ou não;
    - A classe cliente terá um atributo booleano que definirá se ele é preferencial ou não, chamado preferencial.;


'''

from fila import FilaEstatica
from random import randint

class Cliente:
    def __init__(self, preferencial: bool, senha: int) -> None:
        self.preferencial = preferencial
        self.senha = senha

class Caixa:

    senhas: int = []

    def __init__(self, quantidade: int) -> None:
        if quantidade >= 2 and quantidade <= 20:
            self.quantidade = quantidade
        else:
            raise ValueError('Só serão permitidos de 2 a 20 caixas para o atendimento.')

    def geraSenha(self, cliente: Cliente) -> int:
        if len(self.senhas) <= self.quantidade
            cliente.senha = randint(0, self.quantidade)
            self.senhas.append(cliente.senha)
        else:

def menu():
    print('------- SIMULADOR DE ATENDIMENTO DE CLIENTES --------')
    qtdCaixas = input('Digite a quantidade de caixas que estarão ativos no mercado:')
    fila_clientes = FilaEstatica(qtdCaixas)
    

def main(args):
    menu()

if __name__ == '__main__':
    main(sys.argv)
    import doctest
    doctest.testmod()