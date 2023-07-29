palavra = 'abacate'

dicionario = {}

for letra in palavra:
    if letra in dicionario.keys():
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
print(dicionario)