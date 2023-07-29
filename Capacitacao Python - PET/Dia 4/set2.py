import os
clear = lambda: os.system('cls')

resposta = ''
set1 = set()
set2 = set()
i:int = 0

print('Digite a primeira lista: ')
while resposta != 'nao':
    set1.add(input('Digite alguma coisa: '))
    i = i+1
    resposta = input('Deseja continuar? (sim/nao)')

resposta = 'sim'
i = 0

clear()
print('Digite a segunda lista: ')

while resposta != 'nao':
    set2.add(input('Digite alguma coisa: '))
    i = i+1
    resposta = input('Deseja continuar? (sim/nao)')

clear()

print('Valores únicos entre os conjuntos: ')
print(set1 - set2, set2 - set1)
print(set1 ^ set2)
