def modulo(n1:int) -> int:
    if n1 < 0:
        n1 = n1*(-1)
    
    return n1

def entrada():
    n1 = int(input("Digite o número: "))
    mod = modulo(n1)
    print("O módulo do número é: ", mod)

def maximo(n1: int, n2: int) -> int:
    if n1 > n2:
        maior: int = n1
    else:
        maior: int = n2
    return maior

entrada()