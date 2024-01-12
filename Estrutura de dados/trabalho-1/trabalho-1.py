'''
2) Definição dos tipos de dados
    - Os clientes serão representados por uma classe Cliente, que poderá ser preferencial ou não;
    - A classe cliente terá um atributo booleano que definirá se ele é preferencial ou não, chamado preferencial.;


'''

from fila import FilaEstatica
from random import randint
from vetor import Vetor
from typing import List

class Cliente:
    def __init__(self, preferencial: bool, senha: int) -> None:
        self.preferencial = preferencial
        self.senha = senha


class Caixa:
    senhas_clientes: FilaEstatica
    senhas_disponiveis: FilaEstatica

    def __init__(self) -> None:
        self.senhas_clientes = FilaEstatica(10)
        self.senhas_disponiveis = FilaEstatica(10)
        for i in range(1, 10):
            self.senhas_disponiveis.enfileira(i)

    def geraSenha(self, cliente: Cliente) -> int:
        self.senhas_clientes.enfileira(self.senhas_disponiveis.primeiroElemento)

    def disponivel() -> bool:
        return not senhas_clientes.cheia()
class Mercado:
    caixas: List[Caixa]

    def __init__(self, quantidade: int) -> None:
        if quantidade >= 2 and quantidade <= 20:
            self.quantidade = quantidade
            caixas = Vetor(self.quantidade)
            for i in range(1, self.quantidade):
                caixas[i] = Caixa()
        else:
            raise ValueError('Só serão permitidos de 2 a 20 caixas para o atendimento.')
        
    def logistica() -> int:
        ''' Função responsável pela logística do mercado. Verifica qual é o primeiro caixa com vaga disponível e
            retorna a senha para o cliente:
        '''
        disponivel: bool
        i: int = 0
        while not disponivel:
            if self.caixas
            i += 1



def menu():
    print('------- SIMULADOR DE ATENDIMENTO DE CLIENTES --------')
    qtdCaixas = input('Digite a quantidade de caixas que estarão ativos no mercado:')

    mercado = Mercado(qtdCaixas)
    resposta: int
    while resposta != 5:
        print('Digite:')
        print('1) Para retirada de senha; ')
        print('2) Para chamar um Cliente; ')
        print('3) Para consultar os Clientes em espera;')
        print('4) Para consultar o estado dos caixas;')
        print('5) Para sair. ')
        resposta = input()
        if type(resposta) is not int:
            print('Valor inválido. Digite um número das opções acima.')
        elif resposta == 1:
            mercado.logistica()



def main(args):
    menu()

if __name__ == '__main__':
    main(sys.argv)
    import doctest
    doctest.testmod()