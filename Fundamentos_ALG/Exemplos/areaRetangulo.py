def area_retangulo(base, altura: float) -> float:
    return base * altura

def area():
    b = float(input('Digite o valor da base: '))
    a = float(input('Digite o valor da altura: '))
    print('A área do retângulo é: ', area_retangulo(b, a), 'm^2')

area()