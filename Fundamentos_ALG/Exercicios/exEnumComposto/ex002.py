'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Receber o RA, nome, e curso de um aluno;
        - Se a quantidade de dígitos do RA for inválida
        (diferente de 6), então pedir ao usuário para que
        digite novamente, avisando a invalidez do valor.
    - Atribuir esses atributos a um dado composto;
    - Imprimir o dado composto cadastrado.


2) Definição dos tipos de dados
    - O RA será representado pelo tipo inteiro, e o 
    nome e o curso, pelo tipo caractere. E todos esses
    atributos serão atribuídos a um dado composto.
'''

# 3) Especificação

def main():
    '''Método responsável pela entrada dos dados e manipulação
    das funções. '''
    print('-------- CADASTRO ALUNOS - UEM --------')
    RA = input('Digite o seu RA: ')
    nome = input('Digite o seu nome: ')
    curso = input('Digite o seu curso: ')
    dadosAluno = cadastroAluno(entradaAluno(RA, nome, curso))
    
    if dadosAluno != 0:
        relatorioAluno(dadosAluno)


def entradaAluno(RA: int, nome: str, curso: str):
    '''Recebe o RA, nome e curso de um aluno, e retorna
        esses valores em um array do tipo caractere, caso
        o RA seja válido. Caso contrário, retorna 'RA inválido.'.

        Exemplos:
        >>> entradaAluno(143302, 'Bruno HP', 'Informática')
        ['143302', 'Bruno HP', 'Informática']
        >>> entradaAluno(2, 'Ronaldo', 'Engenharia Textil')
        'RA inválido.'
    '''
    # 4.0) Implementação
    if len(str(RA)) != 6:
        return 'RA inválido.'
    else:
        return [str(RA), nome, curso]

from dataclasses import dataclass
@dataclass
class Aluno:
    RA: int
    nome: str
    curso: str

def cadastroAluno(dadosAluno: str) -> Aluno:
    '''Lê o RA, nome e curso do aluno e, caso o RA
        seja válido, transforma os atributos do aluno
        em um dado composto, e retorna esse valor.

        Exemplos:
        >>> cadastroAluno(['143302', 'Bruno HP', 'Informática'])
        Aluno(RA=143302, nome='Bruno HP', curso='Informática')
        >>> cadastroAluno('RA inválido.')
        0
    '''
    # 4.1) Implementação

    if dadosAluno != 'RA inválido.':
        pessoa = Aluno(int(dadosAluno[0]), dadosAluno[1], dadosAluno[2])
        return pessoa
    else:
        return 0

def relatorioAluno(entrada: Aluno):
    '''
        Imprime o dado composto do Aluno no terminal.
    '''
    # 4.2) Implementação
    print('RA: ', entrada.RA)
    print('Nome: ', entrada.nome)
    print('Curso: ', entrada.curso)

# 5) Verificação
if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()

''' 6. Revisão: Foi necessário refazer o relatório de alunos
    devido a alguns erros.
'''