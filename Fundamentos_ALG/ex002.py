temperaturaF = float(input("Digite a temperatura em Farenheit: "))
temperaturaC = (temperaturaF-32)*(5/9)
print("A temperatura em Celsius é: ", temperaturaC)
if temperaturaC>25:
    print("Está calor!")
elif temperaturaC>=17 and temperaturaC<=25:
    print("O clima está agradável.")
elif temperaturaC<17:
    print("Está frio!")