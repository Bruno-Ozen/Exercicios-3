def leFrase():
    frase = input('Digite uma frase: ')
    n = int(input('Digite um número: '))
    print('string produzida = ', exclamacao(frase, n))

def exclamacao(frase:str, n:int) -> str:
    return frase+('!'*n)

leFrase()