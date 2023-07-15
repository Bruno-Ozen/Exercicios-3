# Bibliotecas
import os
clear = lambda: os.system('cls')

print('----------- CALCULADORA -------------')
print('N1 = ? , N2 = ?')
n1 = int(input("Digite o valor de N1: "))
n2 = int(input("Digite o valor de N2: "))
clear()
print('----------- CALCULADORA -------------')
print('N1 = ', n1, ',', 'N2 = ', n2)
print('Digite a operação que deseja realizar entre N1 e N2: ')
print('(+) - Para soma;')
print('(-) - Para subtração;')
print('(x) - Para multiplicação;')
print('(/) - Para divisão;')

continua: bool = True
while continua:
    operacao = input()
    if operacao == '+':
        soma = n1+n2
        print('N1 + N2 = ', soma)
    elif operacao == '-':
        subtracao = n1-n2
        print('N1 - N2 = ', subtracao)
    elif operacao == 'x':
        multiplicacao = n1*n2
        print('N1 * N2 = ', multiplicacao)
    elif operacao == '/':
        divisao = n1/n2
        print('N1 / N2 = ', divisao)
    simounao = (input('Deseja continuar? (s/n)'))
    if simounao == 's':
        continua = True
        continue
    elif simounao == 'n':
        continua = False
clear()
print('------ Obrigado por usar o meu programa :) ------')