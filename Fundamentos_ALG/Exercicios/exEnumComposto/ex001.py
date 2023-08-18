'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Ler como entrada a cor atual de um semáforo,
    converte-la em um tipo enumerado, podendo ser vermelho,
    amarelo ou verde. Retornar a próxima cor do semáforo
    se os dados de entrada forem válidos.

2) Definição dos tipos de dados
    - As cores do semáforo serão representadas por um tipo
    enumerado, que serão a saída do programa. Já a entrada
    se dará pelo tipo caractére.
'''

# 3) Especificação
from enum import Enum, auto

class Semaforo(Enum):
    VERMELHO = auto()
    AMARELO = auto()
    VERDE = auto()
    INVALIDO = auto()

def converteCor(cor: str) -> Semaforo:
    if cor.upper() == Semaforo.VERMELHO.name:
        return Semaforo.VERMELHO
    elif cor.upper() == Semaforo.AMARELO.name:
        return Semaforo.AMARELO
    elif cor.upper() == Semaforo.VERDE.name:
        return Semaforo.VERDE
    else:
        return Semaforo.INVALIDO

def proximoSemaforo(cor: str) -> Semaforo:
    '''Recebe a cor atual de um semáforo em
        string e devolve a próxima cor que 
        será ativada.

        Exemplos:
        >>> proximoSemaforo("Vermelho").name
        'AMARELO'
        >>> proximoSemaforo("Verde").name
        'VERMELHO'
        >>> proximoSemaforo("Perenaldo").name
        'INVALIDO'
    '''
    # 4) Implementação
    corSemaforo = converteCor(cor)
    if corSemaforo.name == Semaforo.VERMELHO.name:
        return Semaforo.AMARELO
    elif corSemaforo.name == Semaforo.VERDE.name:
        return Semaforo.VERMELHO
    elif corSemaforo.name == Semaforo.VERMELHO.name:
        return Semaforo.VERDE
    else:
        return Semaforo.INVALIDO

# 5) Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Após sessões de dor e sofrimento, foi constatado que
    o erro do código era a maneira que os elementos do ENUM
    eram declarados, no caso eu estava usando ponto e vírgula (;),
    e na verdade usa-se igual (=).'''
