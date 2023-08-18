'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Receber um número inteiro que representa um intervalo de tempo
    medido em minutos e devolver uma estrutura contendo o número equivalente
    de horas e minutos.

2) Definição dos tipos de dados
    - As horas e minutos serão representadas pelo tipo inteiro,
    enquanto a estrutura se dará por um dado composto.
'''

# 3) Especificação
from dataclasses import dataclass
@dataclass
class Horas:
    horas: int
    minutos: int

def converteMinutos(minutos: int) -> Horas:
    '''Recebe o RA, nome e curso de um aluno, e retorna
    esses valores em um array do tipo caractere, caso
    o RA seja válido. Caso contrário, retorna 'RA inválido.'.

    Exemplos:
    >>> converteMinutos(131)
    Horas(horas=2, minutos=11)
    >>> converteMinutos(-30)
    Horas(horas=0, minutos=0)
    >>> converteMinutos(24000)
    Horas(horas=400, minutos=0)

    '''
    # 4) Implementação
    if minutos > 0:
        horas: int = 0
        while(minutos-60) >= 0:
            minutos = minutos - 60
            horas = horas + 1
        return Horas(horas, minutos)
    else:
        return Horas(0, 0)
# 5) Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Foi necessário corrigir a função ConverteMinutos,
    mudando o que era antes um maior (>), que retornava 
    399 horas no caso de 24000 minutos, para um
    maior igual (>=), que retorna 400, a valor correto
    para a função.
'''