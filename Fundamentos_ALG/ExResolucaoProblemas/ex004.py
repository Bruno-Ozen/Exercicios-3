'''
Aluno: Bruno Henrique de Pinho
RA: 133301

EXERCÍCIO 4
1. Análise
	- Receber a média final de um aluno e retornar o seu conceito, sendo:
    de 0,0 a 4,9: D;
    de 5,0 a 6,9: C;
    de 7,0 a 8,9: B;
    de 9,0 a 10,0: A.
    - Em caso de número acima de 10, ou negativo, retorna 'Valor inválido.'

2. Definição dos tipos de dados
	- O valor de entrada da média final do aluno será representado pelo
    tipo real, enquanto o de saída, sendo o mesmo a letra correspondente
    ao conceito do aluno, representado pelo tipo caractere.
'''

# 3. Especificação:
def retornaConceito(nota: float) -> str:
    '''Lê a nota final do aluno e retorna o seu conceito.

        Exemplos: 
        >>> retornaConceito(8.5)
        'B'
        >>> retornaConceito(3.2)
        'D'
        >>> retornaConceito(-42)
        'Valor inválido.'
        >>> retornaConceito(7.0)
        'B'
    '''
    # 4. Implementação
    if nota >= 0 and nota <= 10:
        if nota < 5.0:
            return 'D'
        elif nota < 7.0:
            return 'C'
        elif nota < 9.0:
            return 'B'
        else:
            return 'A'
    else:
        return 'Valor inválido.'

# 5. Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Nenhuma modificação foi necessária.'''