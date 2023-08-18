'''
Aluno: Bruno Henrique de Pinho
RA: 133301

1) Análise
    - Projetar uma função que lê uma palavra
    e a partir dessa entrada classifica um nome
    de acordo com seu número de letras, sendo:
        - Curto quando menor ou igual a 4;
        - Mediano quando maior que 4 e menor que 8;
        - Longo quando maior ou igual a 8.
    - Espaços em branco não serão considerados;
        - Portanto, o tipo caractere será formatado
        sem os espaços para que sejam contados as letras
        do nome.
    *Nota: Caso a entrada da função
    não for um nome, como um número por exemplo,
    então o programa retornará o tipo inválido.
    
2) Definição dos tipos de dados
    - A palavra de entrada será representada pelo tipo
    caractere, enquanto o tipo da palavra será representado
    por um tipo enumerado.
'''

# 3) Especificação
from enum import Enum, auto

class TipoPalavra(Enum):
    CURTO = auto()
    MEDIO = auto()
    LONGO = auto()
    INVALIDO = auto()

def removeEspacos(nome: str) -> str:
    '''Recebe um nome e formata-o removendo
    os espaços em um novo tipo caractere. Se
    não houver espaços, retorna igual.

        Exemplos:
        >>> removeEspacos('José Luiz Silva')
        'JoséLuizSilva'
        >>> removeEspacos('Vania')
        'Vania'
        >>> removeEspacos(' ')
        ''
    '''
    # 4) Implementação
    nomeFormatado: str = ''
    for i in nome:
        if i != ' ':
            nomeFormatado = nomeFormatado + i
            
    return nomeFormatado

def classificaPalavra(nome: str) -> TipoPalavra:
    '''Recebe um nome e classifica o mesmo
        de acordo com seu número de letras, sendo:
        - Curto quando menor ou igual a 4;
        - Mediano quando maior que 4 e menor que 8;
        - Longo quando maior ou igual a 8.
        Caso o nome seja inválido, retorna o tipo inválido.

        Exemplos:
        >>> classificaPalavra('Luiz Ronaldo Fenomeno').name
        'LONGO'
        >>> classificaPalavra('12213123123').name
        'INVALIDO'
        >>> classificaPalavra('Luiz').name
        'CURTO'
        >>> classificaPalavra('São João').name
        'MEDIO'
    '''
    # 4) Implementação
    if str.isnumeric(nome):
        return TipoPalavra.INVALIDO
    else:
        nome = removeEspacos(nome)
        if len(nome) <= 4:
            return TipoPalavra.CURTO
        elif len(nome) >= 8:
            return TipoPalavra.LONGO
        else:
            return TipoPalavra.MEDIO

# 5) Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Tive que criar uma função adicional para remover
    os espaços dos nomes, para que o programa contasse
    adequadamente quantas letras tem no nome, já que
    o replace(' ', '') não estava funcionando. Descobri
    isso verificando, por precaução, se nomes de 7 letras
    com 1 espaço eram contados com 7 letras ou 8. Apenas
    o len() estava retornando 8, então assim houve a
    necessidade da correção.
'''