def retornaMaximo2num(a, b: int) -> int:
    if a > b:
        return a
    else:
        return b


# Faça uma função que retorne o máximo entre 3 números.

# Máximo entre uma lista de n números

def retornaMaximo3num(a, b, c: int) -> int:
    max: int = retornaMaximo2num(a, retornaMaximo2num(b, c))
    return max

print(retornaMaximo2num(3, 1000))
print(retornaMaximo3num(3, 1000, 4))