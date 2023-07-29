matriz = []
n:int = 0
k:int = 0
cont:int = 1

for i in range(3):
    aux = []
    for j in range(3):
        aux.append(0)
    matriz.append(aux)

while n<3:
    while k<3:
        matriz[n][k] = cont
        cont = cont + 1
        k = k+1
    n = n+1
    k = 0

print(matriz)