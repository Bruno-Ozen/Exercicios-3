def modulo(n1:int) -> int:
    if n1 < 0:
        n1 = n1*(-1)
    
    return n1

def entrada():
    n1 = int(input("Digite o número: "))
    mod = modulo(n1)
    print("O módulo do número é: ", mod)

entrada()