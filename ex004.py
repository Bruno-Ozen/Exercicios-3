class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

        #Apresentação da pessoa
    def printa_tipo(self):
        print("O tipo da variável Nome é: ", type(self.nome))
        print("O tipo da variável Idade é: ", type(self.idade))
        print("O tipo da variável CPF é: ", type(self.cpf))
nome: str = input("Qual é o seu nome? ")
idade: int = int(input("Qual é a sua idade? "))
cpf: str = input("Qual é o seu CPF? (XXX.XXX.XXX-XX) ")
pessoa = Pessoa(nome, idade, cpf)
pessoa.printa_tipo()