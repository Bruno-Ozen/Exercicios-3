from enum import Enum, auto
from dataclasses import dataclass

class Semaforo(Enum):
    VERMELHO = auto()
    AMARELO = auto()
    VERDE = auto()
    INVALIDO = auto()

print(Semaforo.VERMELHO) 