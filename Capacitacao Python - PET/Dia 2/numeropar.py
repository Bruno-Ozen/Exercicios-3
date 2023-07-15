print('------ Números pares de 0 a 10 ------')
i = 0
while i <= 10:
    if i%2 == 0:
        print(i)
    i = i+1

print('------ Números pares de 0 a n ------')
n = int(input('Digite até qual valor você quer que eu conte os valores pares: '))
i = 0
while i <= n:
    if i%2 == 0:
        print(i)
    i = i+1