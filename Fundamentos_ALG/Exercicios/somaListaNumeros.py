def main():
    lista = [1, 4, 100, 72, 80]
    print(somaListaNumeros(lista))
    print(maxValorLista(lista))

'''Faça uma função que receba uma lista de números inteiros
e retorne a soma desses elementos
I Exemplo: L = [2,5,1,7] → Soma = 2 + 5 + 1 + 7 = 15
'''
def somaListaNumeros(numeros: int) -> int:
    soma: int = 0
    for i in numeros:
        soma = soma + i
    return soma

'''Projete uma função que encontre o valor máximo de uma
lista com 5 números
I Exemplo: L = [4,2,6,7,1] → Máximo = 7
'''

def maxValorLista(numeros: list) -> int:
    maior: int = numeros[0]
    for i in numeros:
        if i > maior:
            maior = i
    return maior

if __name__ == "__main__":
    import doctest
    main()
    doctest.testmod()