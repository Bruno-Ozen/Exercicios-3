n = int(input('Digite um número inteiro: '))
fatorial = 1

for i in range(1, (n+1)):
    fatorial = fatorial*i
print('O fatorial de ', n, 'é ', fatorial)