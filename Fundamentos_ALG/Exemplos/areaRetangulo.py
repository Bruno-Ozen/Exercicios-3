def area_retangulo(base, altura: float) -> float:
    return base * altura

def area():
    b = float(input('Digite o valor da base: '))
    h = float(input('Digite o valor da altura: '))
    area: float = area_retangulo(b, h)
    print('A área do retângulo é: ', area, 'm^2')

area()