import os
clear = lambda: os.system('cls')

numeros = []
aux: int
ordem: str = ''
resposta: str = ''

print('----- Bem vindo ao ordenador Bubblesort em Python! -----')
print('----------------- INSERINDO SUA LISTA ------------------')
while resposta != 'n':
    numeros.append(int(input('Digite um número: ')))
    resposta = input('Deseja continuar? (s/n)')
clear()

while ordem != 'cresc' or ordem != 'desc':
    ordem = input('Em qual ordem deseja ordenar? ("cresc" para crescente, e "desc" para decrescente)')
    if(ordem == 'cresc' or ordem == 'desc'):
        break
clear()

# Ordenando
for i in range(0, len(numeros)):
    for j in range(0, len(numeros)-1):
        if numeros[j]>numeros[j+1] and ordem == 'cresc':
            aux = numeros[j+1]
            numeros[j+1] = numeros[j]
            numeros[j] = aux
        if numeros[j]<numeros[j+1] and ordem == 'desc':
            aux = numeros[j+1]
            numeros[j+1] = numeros[j]
            numeros[j] = aux

#Saída da lista ordenada
print('----- LISTA ORDENADA -----')
for i in numeros:
    print(i)