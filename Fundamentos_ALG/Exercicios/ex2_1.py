def leNumero():
    n = float(input('Digite um número: '))
    porc = float(input('Digite uma porcentagem: '))
    print('Resultado produzido: ', aumenta(n, porc))

def aumenta(n, porc: float) -> float:
    return n*(1+porc/100)

leNumero()