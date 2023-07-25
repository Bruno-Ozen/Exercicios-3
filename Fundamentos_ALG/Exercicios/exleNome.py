# Faça uma função que leia o nome de uma pessoa e chame
# uma segunda função que verifique se o primeiro nome da pessoa é
# "Maria" (true ou false). A primeira função deve informar esse
# retorno para o usuário.

def verificaMaria(nome: str) -> bool:
    maria = nome.split(' ')
    return maria[0] == 'Maria'

def verificaSilva(nome: str) -> bool:
    silva = nome.split(' ')
    return silva[len(silva)-1] == 'Silva'

def verificaSilva2(nome: str) -> bool:
    return nome[len(nome)-5:len(nome)] == 'Silva'

def verificaMaria2(nome: str) -> bool:
    return nome[0:5] == 'Maria'


def leNome():
    nome = input("Digite o seu nome: ")
    eMaria: bool = verificaMaria(nome)
    eMaria2: bool = verificaMaria2(nome)
    eSilva: bool = verificaSilva(nome)
    eSilva2: bool = verificaSilva2(nome)
    print("O seu nome é Maria? ", eMaria, eMaria2)
    print("O seu último nome é Silva? ", eSilva, eSilva2)

leNome()

# Faça uma função que leia o nome de uma pessoa e chame
# uma segunda função que verifique se o último sobrenome da pessoa é
# "Silva"