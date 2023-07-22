def retornaPares(n:int):
    j:int = 0
    numerosPares:int = []

    for i in range(0, n+1):
        if i%2 == 0:
            numerosPares.append(i)
        j = j+1
    return numerosPares

def retornaImpares(n:int):
    j:int = 0
    numerosImpares:int = []

    for i in range(0, n+1):
        if i%2 == 1:
            numerosImpares.append(i)
        j = j+1
    return numerosImpares

n = int(input('Digite um número: '))
print('Deseja imprimir os números pares ou ímpares até ', n, '?')
resposta = input()
print('("pares" para par e "impares" para ímpar)')
if resposta == 'pares':
    for i in retornaPares(n):
        print(i)
if resposta == 'impares':
    for i in retornaImpares(n):
        print(i)