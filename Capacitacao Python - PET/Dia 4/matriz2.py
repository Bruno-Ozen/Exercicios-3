import os
clear = lambda: os.system('cls')

matriz = []
n:int = 0
k:int = 0
soma:int = 0
linhas: int
colunas: int

linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))

for i in range(linhas):
    aux = []
    for j in range(colunas):
        print('Digite um número [', n, ':', k, ']: ')
        aux.append(int(input()))
        k = k+1
    matriz.append(aux)
    n = n+1

n = 0
k = 0

while n<linhas:
    while k<colunas:
        soma = soma + matriz[n][k]
        k = k+1
    n = n+1
    k = 0

clear()
print('MATRIZ')
print(matriz)
print('Soma = ', soma)