# Faça uma função que retorne o máximo entre 3 números.

# Máximo entre uma lista de n números
def retornaMaximo3numeros(a, b, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def retornaMaximoFlex(num: int) -> int:
    maximo: int = num[0]
    for i in num:
        if i > maximo:
            maximo = i
    return maximo

def retornaMaximoFuncao(num: int) -> int:
    return max(num)

def retornaMaximoLista(num: int) -> int:
    i: int = 0
    while len(num) > 1:
        while i<(len(num)-1):
            if num[i]<num[i+1]:
                num.pop(i)
            i = i + 1
    return num

numeros = [1, 52, 3, 10000000, 32, 47, 60, 23, 24, 0, 1, 2, 4049, 2931]
tresNumeros = numeros[0 : 3]

print(retornaMaximoFlex(numeros))
print(retornaMaximo3numeros(2, 42, 1))
print(retornaMaximoFuncao(numeros))          
print(retornaMaximoLista(numeros))  