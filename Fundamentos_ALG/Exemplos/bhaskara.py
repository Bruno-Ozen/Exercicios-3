def calculaDelta(a, b, c) -> float:
    return (b**2)-4*a*c

def calculaX(a, b, c):
    delta = calculaDelta(a, b, c)
    if delta<0:
        print('Não existem raizes reais para esses valores de A, B, C. ')
    elif delta>0:
        raizes = [(-b+(delta)**(1/2))/(2*a),(-b-(delta)**(1/2))/(2*a)]
        return raizes
    elif delta==0:
        raiz = (-b+(delta)**(1/2))/(2*a)
        return raiz
    
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
print('As raizes desses valores é: ', calculaX(a, b, c))