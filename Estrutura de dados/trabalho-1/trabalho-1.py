'''
2) Definição dos tipos de dados
    - Os clientes serão representados por uma classe Cliente, que poderá ser preferencial ou não;
    - A classe cliente terá um atributo booleano que definirá se ele é preferencial ou não, chamado preferencial.;


'''

from fila import FilaEstatica
from random import randint
from vetor import Vetor
from typing import List
from dataclasses import dataclass
import sys

@dataclass
class Senha:
    numero_caixa: int
    numero_senha: int

class Cliente:
    def __init__(self, preferencial: bool, senha: Senha) -> None:
        self.preferencial = preferencial
        self.senha = senha

class Caixa:
    # Número do caixa
    numero: int
    # Fila estática de clientes da modalidade Comum
    senhas_clientes: FilaEstatica
    # Fila estática de clioentes da modalidade Preferencial
    senhas_preferencial: FilaEstatica
    # Fila estática de senhas a serem reutilizadas. As três
    # filas deverão ter o mesmo tamanho.
    senhas_disponiveis: FilaEstatica

    def __init__(self, numero) -> None:
        self.numero = numero
        self.senhas_clientes = FilaEstatica(10)
        self.senhas_preferencial = FilaEstatica(10)
        self.senhas_disponiveis = FilaEstatica(10)
        for i in range(1, 10):
            self.senhas_disponiveis.enfileira(Senha(self.numero, i))

    def geraSenha(self, preferencial) -> None:
        senha: Senha = self.senhas_disponiveis.desenfileira()
        if preferencial:
            self.senhas_preferencial.enfileira(senha)
        else:
            self.senhas_clientes.enfileira(senha)

    def atender(self, preferencial) -> Senha:
        if preferencial and not self.senhas_preferencial.vazia():
            return self.senhas_preferencial.desenfileira()
        elif not preferencial and not self.senhas_clientes.vazia():
            return self.senhas_clientes.desenfileira()
        else:
            return Senha(0, 0)

    def disponivel(self) -> bool:
        return not self.senhas_clientes.cheia()

    def preferencial_vazia(self) -> bool:
        return not self.senhas_preferencial.cheia()

    def comum_vazia(self) -> bool:
        return not self.senhas_clientes.cheia()
    
class Mercado:
    caixas: List[Caixa]

    def __init__(self, quantidade: int) -> None:
        if quantidade >= 2 and quantidade <= 20:
            self.quantidade = quantidade
            self.caixas = []
            for i in range(self.quantidade):
                self.caixas.append(Caixa(i + 1))
        else:
            raise ValueError('Só serão permitidos de 2 a 20 caixas para o atendimento. ')

    def logistica(self) -> Cliente:
        ''' Função responsável pela logística do mercado. Verifica qual é o primeiro caixa com vaga disponível e
            retorna a senha para o cliente:
        '''
        disponivel: bool = False
        preferencial: bool
        resposta: str
        senha: Senha = Senha(0, 0)
        i: int = 0

        print('Qual modalidade de atendimento o Sr./Sra. deseja?')
        print('1) Para Comum ')
        print('2) Para Preferencial ')
        resposta = input()
        if int(resposta) == 1:
            preferencial = False
        elif int(resposta) == 2:
            preferencial = True
        else:
            print('Valor inválido. Digite outro número e tente novamente.')
        while not disponivel and i < self.quantidade:
            if self.caixas[i].disponivel():
                self.caixas[i].geraSenha(preferencial)
                disponivel = True
                print('Enfileirado com sucesso!')
            else:
                print('Não há caixas disponíveis no momento.')
                break
            i += 1
        return Cliente(preferencial, senha)
    
    def chama_cliente(self, caixa: int) -> Senha:
        '''Chama um cliente, exibindo a senha, modalidade e caixa na tela. Retorna a senha chamada,
            para que seja reutilizada posteriormente na fila de senhas_disponiveis.
        '''
        if self.caixas[caixa].preferencial_vazia():
            cliente = self.caixas[caixa].atender(False)
            print('------ ATENÇÃO! Cliente de senha:', cliente.senha.numero_senha, '------')
            print('------- Caixa:', self.caixas[caixa].numero)
            print('De modalidade: Comum. Comparecer caixa para o atendimento.')
        elif not self.caixas[caixa].senhas_preferencial.vazia():
            cliente = self.caixas[caixa].atender(True)
            print('------ ATENÇÃO! Cliente de senha:', cliente.senha.numero_senha, '------')
            print('------- Caixa:', self.caixas[caixa].numero)
            print('De modalidade: Preferencial. Comparecer caixa para o atendimento.')
        else:
            print('Não há nenhum cliente em fila no momento.')
            return Senha(0, 0)

def menu():
    print('------- SIMULADOR DE ATENDIMENTO DE CLIENTES --------')
    qtdCaixas = int(input('Digite a quantidade de caixas que estarão ativos no mercado:'))
    mercado = Mercado(qtdCaixas)
    resposta: int = 0

    while resposta != 5:
        print('Digite:')
        print('1) Para retirada de senha; ')
        print('2) Para chamar um Cliente; ')
        print('3) Para consultar os Clientes em espera; ')
        print('4) Para consultar o estado dos caixas; ')
        print('5) Para sair. ')
        resposta = int(input())
        if type(resposta) is not int:
            print('Valor inválido. Digite um número das opções acima. ')
        elif resposta == 1:
            cliente = mercado.logistica()
            print('Senha: ', cliente.senha.numero_senha)
            print('Caixa: ', cliente.senha.numero_caixa)
        elif resposta == 2:
            caixa = int(input('Qual é o número do caixa que deseja chamar? '))
            senha_reciclada = mercado.chama_cliente(int(caixa))
            mercado.caixas[caixa].senhas_disponiveis.enfileira(senha_reciclada)
        elif resposta == 3:
            caixa = int(input('Qual é o número do caixa que deseja consultar a fila de Clientes?'))
            print('Fila de Clientes Comuns:')
            mercado.caixas[caixa].senhas_clientes.exibe()
            print('Fila de Clientes Preferenciais:')
            mercado.caixas[caixa].senhas_preferencial.exibe()
        elif resposta == 4:
            print('------- Caixas do Super Mercado -------')
            # Caixa -> Variável responsável por ser o índice para que o for percorra todos os caixas
            for i in range (qtdCaixas):
                if not mercado.caixas[i].senhas_preferencial.vazia():
                    print('Caixa ', i, ': Atendendo a senha Preferencial -', mercado.caixas[i].senhas_preferencial.primeiroElemento().senha)
                if not mercado.caixas[i].senhas_clientes.vazia():
                    print('Caixa ', i, ': Atendendo a senha Comum -', mercado.caixas[i].senhas_clientes.primeiroElemento().senha)
        elif resposta == 5:
            print('Obrigado pela preferência. Tenha uma boa tarde/noite!')
        else:
            print('Número inválido. Digite outro valor e tente novamente.')

def main(args):
    menu()

if __name__ == '__main__':
    main(sys.argv)
    import doctest
    doctest.testmod()