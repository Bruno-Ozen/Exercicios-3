entrada = input("Digite qualquer coisa, e eu imprimirei quantas vezes quiser no terminal! ")
qtd = int(input("Quantas vezes quer imprimir " + entrada + " no terminal?"))
for i in range(qtd):
    print(i+1, ".", entrada, "\n")