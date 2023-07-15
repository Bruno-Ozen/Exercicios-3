class Pessoa:
    def __init__(self, usuario, idade, comida_favorita):
        self.usuario = usuario
        self.idade = idade
        self.comida_favorita = comida_favorita

        #Apresentação da pessoa
        print("")
        print("Olá, meu  é " + self.usuario)
        print("Minha idade é ", self.idade, " anos")
        print("E a minha comida favorita é ", self.comida_favorita)

nome: str = input("Qual é o seu nome? ")
idade: int = int(input("Qual é a sua idade? "))
comidafav: str = input("Qual é a sua comida favorita? ")
pessoa = Pessoa(nome, idade, comidafav)