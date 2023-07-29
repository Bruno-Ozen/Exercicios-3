notas = {
    'Luizinho' : 45,
    'Joãozinho' : 76,
    'Robertinho' : 10,
    'Osmarzinho' : 100,
    'Little Robert' : 60
}

def calculaMedia(nota:float):
    soma:float = 0
    for i in nota:
        soma = soma + i
    return soma/len(nota)

print('A média é: ', calculaMedia(notas.values()))