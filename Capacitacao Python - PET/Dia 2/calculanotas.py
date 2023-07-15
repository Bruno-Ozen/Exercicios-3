notas = [47, 32, 90, 100, 77, 53, 38, 96] 
vermelho = 0
azul = 0

for nota in notas:
    if nota>=60:
        azul = azul + 1
    elif nota<60 or nota>=0:
        vermelho = vermelho + 1
print('Na lista informada, temos: ')
print(azul, 'notas azuis; ')
print(vermelho, 'notas vermelhas.')