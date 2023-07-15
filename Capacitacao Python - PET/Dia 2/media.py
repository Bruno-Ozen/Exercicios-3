# Bibliotecas
import os
clear = lambda: os.system('cls')

print('CALCULADORA DE MÉDIA')
print('Digite os valores aos quais deseja calcular a média. Para parar, digite -1')
i = 0
anterior: float = 0
media: float = 0
continua = True
n: float = 0
while continua:
    print('Valor ', i+1, ': ')
    n = float(input())
    if n != -1:
        n = (n+anterior)
        media = n/(i+1)
        anterior = n
    clear()
    print('Média = ', media)
    if i>0 and n == -1:
        break
    i = i+1
print('------ Obrigado por usar o meu programa :) ------')