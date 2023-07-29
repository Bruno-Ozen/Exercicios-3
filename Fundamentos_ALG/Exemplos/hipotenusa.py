def calcula_hipotenusa(b, c) -> float:
    return ((b**2)+(c**2))**(1/2)

def triangulo():
    cateto1 = float(input('Digite o valor do catedo oposto: '))
    cateto2 = float(input('Digite o valor do cateto adjacente: '))
    hipotenusa = calcula_hipotenusa(cateto1, cateto2)
    print('Hipotenusa = ', hipotenusa)

triangulo()