n = int(input('Digite um número: '))
fibonacci:str = ''
atual:int = 1
anterior: int = 0
soma:int = 0

for i in range(0, n):
    if i<(n-1):
        fibonacci = fibonacci + str(anterior) + ', '
    if i==(n-1):
        fibonacci = fibonacci + str(anterior) + '.'
        break
    soma = atual+anterior
    anterior = atual
    atual = soma
print(fibonacci)
