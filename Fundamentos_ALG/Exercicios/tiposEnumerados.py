from enum import Enum, auto
from dataclasses import dataclass

class Combustivel(Enum):
    ALCOOL = auto() # Associa os valores a um índice numérico
    GASOLINA = auto() # Definir os tipos enumerados em caixa alta
    '''- O índice começa de 1, não de 0. '''

def indica_combustivel(preco_alcool: float, preco_gasolina: float) -> Combustivel:
    if preco_alcool <= 0.7 * preco_gasolina:
        combustivel = Combustivel.ALCOOL
    else:
        combustivel = Combustivel.GASOLINA
    return combustivel

def programa():
    print(indica_combustivel(4, 5))

programa()