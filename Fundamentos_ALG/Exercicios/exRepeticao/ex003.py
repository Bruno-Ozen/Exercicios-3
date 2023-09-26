'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Projetar uma função que receba como entrada uma lista
    não vazia de votos e determina qual foi o resultado da
    eleição;
        - Se a lista for vazia, então retorna None
        - Se os votos em branco forem mais do que 50% do total
        de votos, novas eleições deverão ser convocadas.
    - Desenvolver uma função auxiliar que conta votos de um
    tipo especificado por parâmetro.

2) Definição dos tipos de dados
    - As opções de voto serão representadas por um tipo enumerado
    chamado VoteOptions, onde haverão as seguintes opções de candidatos:
        - OSMAR, dígito 50
        - ROSELIA, dígito 43
        - BRANCO, dígito 0
    - A entrada da função contaVotos será uma lista de votos, onde cada voto
    é um número inteiro, que é o número do candidato. A saída será uma String 
    que constatará o resultado das eleições;
    - Nas duas funções haverão 3 variáveis numéricas do tipo inteiro para contar os votos: 
    osmar, roselia e branco. Essas estarão num array, sendo ele a entrada da função resultado eleição, nomeado "votosPorCandidato".
'''

# 3) Especificação
from enum import Enum, auto
    
class VoteOptions(Enum):
    CANDIDATO_1 = 50
    CANDIDATO_2 = 43
    BRANCO = 0

from dataclasses import dataclass

@dataclass
class Candidato:
    tipo: VoteOptions
    nome: str
    votos: int

def totalCandidatos(votosPorCandidato: Candidato) -> int:
    '''Calcula o total de votos obtidos na eleição, somando todos
    os itens da lista de votos.
    
    Exemplos:
    >>> totalCandidatos([Candidato(tipo=VoteOptions.CANDIDATO_1, nome='Osmar', votos=40), Candidato(tipo=VoteOptions.CANDIDATO_2, nome='Rosélia', votos=60), Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=30)])
    130
    >>> totalCandidatos([]) is None
    True
    '''
    
    total: int = 0
    if len(votosPorCandidato) > 0:
        for i in votosPorCandidato:
            total = total + i.votos
        return total
    else:
        return None

def validaEleicao(votosPorCandidato: Candidato) -> bool:
    # Index do candidato branco
    brancoIndex: int
    # Index que percorrerá a lista votosPorCandidato
    i: int = 0

    if len(votosPorCandidato) > 0:
        if len(votosPorCandidato) == 1:
            return False
        while i < len(votosPorCandidato):
            if votosPorCandidato[i].tipo == VoteOptions.BRANCO:
                brancoIndex = i
            i = i + 1
        if brancoIndex is not None and votosPorCandidato[brancoIndex].votos / totalCandidatos(votosPorCandidato) <= 0.5:
            return True
        else:
            return False
    else:
        return None


def resultadoEleicao(votosPorCandidato: Candidato) -> str:
    '''Retorna o resultado da eleição a partir da quantidade
    de votos de cada candidato. Se receber como parâmetro o vazio,
    então também retorna vazio. Se os votos em branco forem maiores
    que 50% do total de votos, então solicita a convocação de novas
    eleições. Se os votos dos dois candidatos forem iguais, então
    retorna empate.

    Exemplos:
    >>> resultadoEleicao([Candidato(tipo=VoteOptions.CANDIDATO_1, nome='Osmar', votos=2), Candidato(tipo=VoteOptions.CANDIDATO_2, nome='Rosélia', votos=1), Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=2)])
    'O candidato eleito é Osmar, número 50.'
    >>> resultadoEleicao([Candidato(tipo=VoteOptions.CANDIDATO_1, nome='Osmar', votos=40), Candidato(tipo=VoteOptions.CANDIDATO_2, nome='Rosélia', votos=60), Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=30)])
    'O candidato eleito é Rosélia, número 43.'
    >>> resultadoEleicao([Candidato(tipo=VoteOptions.CANDIDATO_1, nome='Osmar', votos=30), Candidato(tipo=VoteOptions.CANDIDATO_2, nome='Rosélia', votos=30), Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=30)])
    'Empate. Novas eleições deverão ser convocadas.'
    >>> resultadoEleicao([Candidato(tipo=VoteOptions.CANDIDATO_1, nome='Osmar', votos=20), Candidato(tipo=VoteOptions.CANDIDATO_2, nome='Rosélia', votos=30), Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=150)])
    'Eleição inválida. Novas eleições deverão ser convocadas.'
    >>> resultadoEleicao([]) is None
    True
    >>> resultadoEleicao([Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=150)])
    'Eleição inválida. Novas eleições deverão ser convocadas.'
    '''
    if len(votosPorCandidato) > 0:
        # Chama a função validaEleicao, para verificar se o número de candidatos
        # não brancos é maior do que 1, e se a quantidade de brancos é menor ou
        # igual a 50%, para assim validar a eleição e encontrar o candidato eleito.
        if validaEleicao(votosPorCandidato):
            eleito: Candidato
            for i in votosPorCandidato:
                for j in votosPorCandidato:
                    if i.votos < j.votos:
                        break
                    if i.votos >= j.votos:
                        eleito = i
            return 'O candidato eleito é ' + eleito.nome + ', número ' + str(eleito.tipo.value) + '.'
        else:
            return 'Eleição inválida. Novas eleições deverão ser convocadas.'

    else:
        return None
    

    # 4) Implementação

def contaVotos(votos: int, candidatos: Candidato) -> Candidato:
    '''Recebe como entrada uma lista não vazia de votos, de acordo
        com o número do candidato, e determina qual foi o resultado da eleição. 
        Ela faz isso passando por cada termo da lista de votos, adicionando um 
        para cada tipo encontrado.
        
        Exemplos:
        >>> contaVotos([43, 50, 0, 0, 43], [Candidato(tipo=VoteOptions.CANDIDATO_1, nome='Osmar', votos=0), Candidato(tipo=VoteOptions.CANDIDATO_2, nome='Rosélia', votos=0), Candidato(tipo=VoteOptions.BRANCO, nome='Osmar', votos=0)])
        [Candidato(tipo=<VoteOptions.CANDIDATO_1: 50>, nome='Osmar', votos=1), Candidato(tipo=<VoteOptions.CANDIDATO_2: 43>, nome='Rosélia', votos=2), Candidato(tipo=<VoteOptions.BRANCO: 0>, nome='Osmar', votos=2)]
        >>> contaVotos([], []) is None
        True
        >>> contaVotos([], [Candidato(tipo=<VoteOptions.CANDIDATO_1: 50>, nome='Osmar', votos=0), Candidato(tipo=<VoteOptions.CANDIDATO_2: 43>, nome='Rosélia', votos=0), Candidato(tipo=<VoteOptions.BRANCO: 0>, nome='Osmar', votos=0)]) is None
        True
        >>> contaVotos([43, 50, 0, 0, 43], []) is None
        True
        >>> contaVotos([], []) is None
        True
    '''
    if len(votos) > 0 and len(candidatos) > 0:
        i: int = 0
        j: int = 0
        while i < len(votos):
            while j < len(candidatos):
                if votos[i] == candidatos[j].tipo.value:
                    candidatos[j].votos = candidatos[j].votos + 1
                j = j + 1
            i = i + 1
        return candidatos
    else:
        return None
    
# 5) Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    
    '''
