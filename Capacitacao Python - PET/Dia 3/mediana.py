import os
clear = lambda: os.system('cls')

numeros = []
resposta:str = ''

def mediana(numeros:int):
    mediana:float
    i:int = 0
    numeros.sort()
    if len(numeros)%2 == 1:
        index = len(numeros)//2
        return numeros[index]
    else:
        esq = len(numeros)//2-1
        dir = len(numeros)//2
        index = (esq+dir)/2
        return index

print('----------------- INSERINDO SUA LISTA ------------------')
#while resposta != 'n':
   # numeros.append(int(input('Digite um número: ')))
   # resposta = input('Deseja continuar? (s/n)')
#clear()
#print('A mediana da sua lista é ', mediana(numeros))
lista_impar = [1, 2, 3]
lista_par = [1, 2, 3, 4]
par = mediana(lista_par)
impar = mediana(lista_impar)
print('A mediana da lista par é ', par)
print('A mediana da lista ímpar é ', impar)