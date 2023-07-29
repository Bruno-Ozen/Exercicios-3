resposta = ''
lista = []

while resposta != 'nao':
    lista.append(input('Digite alguma coisa: '))
    resposta = input('Deseja continuar? (sim/nao)')

print(list(set(lista)))