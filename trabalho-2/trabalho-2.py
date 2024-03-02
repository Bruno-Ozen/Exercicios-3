from arvoreAVL import AVL
from pessoa import Pessoa

'''
    2) Definição dos tipos de dados:
        - As pessoas cadastradas estarão organizadas hierarquicamente em um TAD de árvore AVL;
        - A classe da árvore AVL foi modificada para receber como elemento do nó, o tipo Pessoa;
        - O tipo Pessoa contém:
            - nome, do tipo caractere (str);
            - idade, do tipo inteiro (int);
            - sexo, do tipo caractere (str);
            - peso, do tipo flutuante (float).
'''

arvore_pessoas = AVL()

def cadastro_simples():
    '''Recebe o nome, idade, sexo e peso de uma única pessoa e cadastra ela, inserindo-a
        em uma árvore AVL.
    '''
    
    # Recebendo os dados:
    print("CADASTRO SIMPLES")
    nome: str = input("Digite o nome da pessoa que deseja inserir: ")
    idade: int = int(input("Digite a idade: "))
    sexo: str = input("Digite o sexo da pessoa (m para masculino e f para feminino: ")
    peso: float = float(input("Digite o peso da pessoa que deseja inserir (em KG): "))
    # Gerando o tipo Pessoa com esses dados:
    pessoa = Pessoa(nome, idade, sexo, peso)
    # Inserindo na árvore AVL:
    arvore_pessoas.insere(pessoa)

    
def cadastro_lote():
    '''Recebe o nome, idade, sexo e peso de várias pessoas, por um input onde os dados de
        cada pessoa é separado por um pipe (|). A função lê, converte, e insere os dados
        em um tipo Pessoa e as insere em uma árvore AVL.
    '''
    # Recebendo os dados:
    print("-----------------------------------------------------------------------------------------------------------")
    print("CADASTRO EM LOTE")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Digite a expressão de cadastro composto, separado por vírgulas (,) e pipes (|) na forma abaixo: ")
    print("nome_1, idade_1, sexo_1, peso_1 | nome_2, idade_2, sexo_2, peso_2 | ... | nome_n, idade_n, sexo_n, peso_n")

    cadastro: str = input()
    pessoas = cadastro.split("|")
    
    for i in pessoas:
        pessoa = i.split(",")
        nome = pessoa[0]
        idade = pessoa[1]
        sexo = pessoa[2]
        peso = pessoa[3]
        arvore_pessoas.insere(Pessoa(nome, idade, sexo, peso))
    
def cadastrar_pessoa():
    # Verifica qual tipo de cadastro será realizado, e efetua o tipo escolhido.
    print("-----------------------------------------------------------------------------------------------------------")
    print("CADASTRO DE PESSOAS")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Qual tipo de cadastro você deseja realizar? ")
    print("1) Cadastro simples")
    print("2) Cadastro em lote")
    escolha = input()
    
    if escolha == "1":
        cadastro_simples()
    elif escolha == "2":
        cadastro_lote()
        

def buscar_pessoa():
    # Recebe o valor que o usuário deseja buscar e efetua uma busca binária na árvore AVL.    
    print("-----------------------------------------------------------------------------------------------------------")
    print("BUSCAR UMA PESSOA")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Qual pessoa você deseja buscar pelo nome? ")
    nome = input()
    nome_buscado = arvore_pessoas.busca(Pessoa(nome, None, None, None))
    if nome_buscado != None:
        print("-----------------------------------------------------------------------------------------------------------")
        print("Pessoa encontrada: ")
        print("Nome: ", nome_buscado.elemento.nome)
        print("Idade: ", nome_buscado.elemento.idade)
        print("Sexo: ", nome_buscado.elemento.sexo)
        print("Peso: ", nome_buscado.elemento.peso)
        print("-----------------------------------------------------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------------------------------------------------")
        print("A pessoa pesquisada não foi encontrada. Tente novamente outra vez. ")
        print("-----------------------------------------------------------------------------------------------------------")
    
def emitir_relatorio():
    '''Percorre a árvore de Pessoas cadastradas in-ordem, de modo que a lista dos nomes cadastrados é
        mostrada em ordem alfabética, junto com o total de pessoas cadastradas, quantidade de homens
        e mulheres no cadastro, o peso médio das pessoas cadastradas e o número de pessoas maiores
        de 18 anos no cadastro.  
    '''
    
    print("-----------------------------------------------------------------------------------------------------------")
    print("RELATÓRIO")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Nome das pessoas cadastradas em ordem alfabética:")
    lista_pessoas = arvore_pessoas.percorreArvoreInOrdem()
    for i in lista_pessoas:
        print(i.elemento.nome)


def main():
    resposta: str = 0
    while resposta != "4":
        print("BEM VINDO AO SISTEMA DE CADASTRO DE PESSOAS!")
        print("-----------------------------------------------------------------------------------------------------------")
        print("Digite: ")
        print("1) Para cadastrar uma pessoa; ")
        print("2) Para buscar uma pessoa; ")
        print("3) Para emitir um relatório; ")
        print("4) Para sair. ")
        resposta = input()
        if resposta == "1":
            cadastrar_pessoa()
        elif resposta == "2":
            buscar_pessoa()
        elif resposta == "3":
            emitir_relatorio()
    print("\nObrigado por utilizar nosso sistema. Tenha um bom dia!")
    
if __name__ == "__main__":
    main()