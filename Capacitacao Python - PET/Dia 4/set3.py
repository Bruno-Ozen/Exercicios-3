import os
clear = lambda: os.system('cls')

def retornaDiferenca(letra:str, a:str, b:str):
    if letra == 'a':
        return a-b
    elif letra == 'b':
        return b-a
    else:
        print('Valores inválidos. ')

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

set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'd', 'e', 'f'}
print('A - B = ', retornaDiferenca('a', set1, set2))
print('B - A = ', retornaDiferenca('b', set1, set2))