paredeMenor = float(input("Digite o tamanho da parede menor: "))
paredeMaior = float(input("Digite o tamanho da parede maior: "))
altura = float(input("Digite a altura da sala: "))
tinta = 12
areaTOT = (altura*paredeMaior*2)+(altura*paredeMenor*2)+(paredeMenor*paredeMaior)
print("A área total da parede é ", areaTOT)
qtdLatas = areaTOT/tinta
print("A quantidade de latas necessárias para pintar essa parede de ", areaTOT, "m é ", qtdLatas)