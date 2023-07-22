import math
def circunferenciaCirculo(raio:float):
    return 2 * math.pi * raio

def areaCirculo(raio:float):
    return math.pi*(raio**2)
raio = float(input('Digite o raio do círculo: '))
print('Circunferência = ', circunferenciaCirculo(raio))
print('Área = ', areaCirculo(raio))