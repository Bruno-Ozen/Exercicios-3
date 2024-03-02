'''
2) Definição dos tipos de dados
    - Os clientes serão representados por uma classe Cliente, que poderá ser preferencial ou não;
    - A classe cliente terá um atributo booleano que definirá se ele é preferencial ou não, chamado preferencial.;

'''

# Nota: Para a implementação a seguir, foi necessário modificar o código da classe FilaEstatica,
# para adequar ela ao exercício.

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
    def __init__(self, numero) -> None:
        self.numero = numero
        self.fila_clientes = FilaEstatica(10)
        self.senhas_disponiveis = FilaEstatica(10)
        for i in range(0, 10):
            self.senhas_disponiveis.enfileira(Senha(self.numero, i + 1))

    def geraSenha(self, preferencial) -> Senha:
        senha: Senha = self.senhas_disponiveis.desenfileira()
        self.fila_clientes.enfileira(Cliente(preferencial, senha))
        return senha

    def atender(self) -> Senha:
        while self.fila_clientes.primeiroElemento().preferencial is not True:
            if self.fila_clientes.primeiroElemento().preferencial == True:
                return self.fila_clientes.desenfileira().senha
            else:
                while i < self.fila_clientes.tamanho() and not self.fila_clientes.preferencial:
                    if self.fila_clientes.preferencial
                        
        else:
            return Senha(0, 0)

    def disponivel(self) -> bool:
        return not self.fila_clientes.cheia()
    
class Mercado:
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
            return Cliente(False, senha)
        
        while not disponivel and i < self.quantidade:
            if self.caixas[i].disponivel():
                senha: Senha = self.caixas[i].geraSenha(preferencial)
                disponivel = True
            i += 1
        if disponivel == False:
            print('Não há caixas disponíveis no momento. Tente novamente mais tarde.')
        return Cliente(preferencial, senha)

    def chama_cliente(self, caixa: int) -> Senha:
        '''Chama um cliente, exibindo a senha, modalidade e caixa na tela. Retorna a senha chamada,
            para que seja reutilizada posteriormente na fila de senhas_disponiveis.
        '''
        senha_cliente = Senha(0, 0)

        if not self.caixas[caixa - 1].senhas_clientes.vazia():
            senha_cliente = self.caixas[caixa - 1].atender()
            if senha_cliente.numero_senha != 0:
                print('------ ATENÇÃO! Cliente de senha:', senha_cliente.numero_senha, '------')
                print('------- Caixa:', self.caixas[caixa - 1].numero)
                print('De modalidade: Comum. Comparecer caixa para o atendimento.')
                if self.caixas[caixa - 1].disponivel():
                    self.caixas[caixa - 1].senhas_disponiveis.enfileira(senha_cliente)
        else:
            print('Não há nenhum cliente em fila no momento.')
        return senha_cliente
    
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
            if cliente.preferencial:
                modalidade = 'Preferencial'
            else:
                modalidade = 'Comum'
            if cliente.senha.numero_caixa != 0 and cliente.senha.numero_senha != 0:
                # modalidade[0] = Inicial da modalidade, podendo ser C para Comum e P para preferencial
                print('Senha: ', cliente.senha.numero_senha, modalidade[0])
                print('Caixa: ', cliente.senha.numero_caixa)
        elif resposta == 2:
            caixa = int(input('Qual é o número do caixa que deseja chamar? '))
            senha_reciclada = mercado.chama_cliente(caixa)
            if senha_reciclada.numero_caixa != 0 and senha_reciclada.numero_senha != 0:
                mercado.caixas[caixa - 1].senhas_disponiveis.enfileira(senha_reciclada)
        elif resposta == 3:
            caixa = int(input('Qual é o número do caixa que deseja consultar a fila de Clientes?'))
            print('------- Fila de Clientes -------')
            mercado.caixas[caixa - 1].senhas_clientes.exibe()
        elif resposta == 4:
            print('------- Caixas do Super Mercado -------')
            # Caixa -> Variável responsável por ser o índice para que o for percorra todos os caixas
            for i in range(qtdCaixas):
                if not mercado.caixas[i].senhas_clientes.vazia():
                    print('Caixa ', str(i + 1), '\nPróximo -', mercado.caixas[i].senhas_clientes.primeiroElemento().senha)
        elif resposta == 5:
            print('Obrigado pela preferência. Tenha uma boa tarde/noite!')
        else:
            print('Número inválido. Digite outro valor e tente novamente.')

def main():
    menu()

if __name__ == '__main__':
    main()