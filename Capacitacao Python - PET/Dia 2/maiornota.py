notas = [47, 32, 90, 100, 77, 53, 38, 96] 
n: int = 0
nota: float
media: float
maior: int = 0
anterior: float = 0

for i in notas:
    nota = (i+anterior)
    media = nota/(n+1)
    anterior = nota
    n = n +1
    if i>maior:
        maior = i
print('A média é ', media)
print('O maior nota é ', maior)