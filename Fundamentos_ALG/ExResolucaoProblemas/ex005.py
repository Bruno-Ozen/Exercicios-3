''' 
Aluno: Bruno Henrique de Pinho
RA: 133301

EXERCÍCIO 5
1. Análise
	- Receber a quantidade de laranjas, e calcular o preço
    total com valor unitário em sua função, sendo R$0.35
    quando abaixo de 12, e R$0.30 se forem compradas pelo
    menos 12. Retornar 'Valor inválido' caso a quantidade seja
    negativa ou 0.

2. Definição dos tipos de dados
	- A entrada de quantidade de laranjas será representada
    por números inteiros, enquanto a saída, e o valor unitário
    da laranja serão representados por números reais na moeda
    real (R$). A quantidade de laranjas será aceita apenas para
    números não negativos acima de 0.
'''

# 3. Especificação:
def calculaLaranja(quantidade: int) -> float:
    '''Calcula o preço unitário em função da quantidade de laranjas
        e após isso, retorna o valor total da compra.

        Exemplos:
        calculaLaranja(5)
        1.75
        calculaLaranja(0)
        'Valor inválido.'
        calculaLaranja(-4)
        'Valor inválido.'
        calculaLaranja(14)
        4.2
    '''
    # 4. Implementação
    valorUnidade: float
    if quantidade > 0:
        if quantidade < 12:
            valorUnidade = 0.35
        else:
            valorUnidade = 0.30
        return valorUnidade * quantidade


# 5. Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Nenhuma modificação foi necessária'''