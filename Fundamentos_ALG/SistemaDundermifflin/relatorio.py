'''1) Análise: Desenvolver um algoritmo que monitore os níveis de estoque da Dunder Mifflin, 
    uma empresa que produz produtos derivados da celulose, para garantir que eles estejam 
    dentro dos limites adequados. O algoritmo também deve:
    - Identificar possíveis casos de rupturas de estoque (quando a demanda
    excede o estoque disponível);
    - Processar os pedidos dos clientes, ou seja, dada uma lista
    contendo os pedidos (produto e quantidade), totalizar a demanda de cada produto;
    - Determinar a receita e o lucro líquido a partir do relatório de vendas;
    - Determinar os três vendedores que geraram mais lucro no mês.
    Cada uma dessas funcionalidades do algoritmo serão representadas por funções.

    Os produtos terão os seguintes preços:
    Produto Quantidade Preço de custo Preço de venda
     Papel   100.000    50,00           60,00
     Papelão  50.000    40,00           48,00
     Painéis  30.000    75,00           90,00
'''

# 2) Definição dos tipos de dados
from dataclasses import dataclass
from enum import Enum, auto

class TipoProduto(Enum):
    BOBINA = auto()
    CHAPA = auto()
    PAINEL = auto()

@dataclass
class Totalizacao:
    tipo: TipoProduto
    quantidade: int
    qtdDesconto: int # Quantidade mínima necessária para a aplicação do desconto
    precoCusto: float
    total: float # Valor de (preço * quantidade) * desconto
    lucro: float
    porcDesconto: float # Porcentagem de desconto

@dataclass
class Pedido:
    produtos: list[Totalizacao]
    precoTotal: float
    cliente: str
    vendedor: str

estoque: list[Totalizacao] = [Totalizacao(tipo=TipoProduto.BOBINA, quantidade=100, qtdDesconto=10, precoCusto=50.0, total=5280.0, lucro=10.0, porcDesconto=12.0),
                                Totalizacao(tipo=TipoProduto.CHAPA, quantidade=50, qtdDesconto=8, precoCusto=40.0, total=2208.0, lucro=8.0, porcDesconto=8.0),
                                Totalizacao(tipo=TipoProduto.PAINEL, quantidade=30, qtdDesconto=10, precoCusto=75.0, total=2295.0, lucro=15.0, porcDesconto=15.0)]

def somaListaInt(numeros: list[int]) -> int:
    '''Soma todos os valores de uma lista e retorna o valor.
    
        Exemplos:
        >>> somaListaInt([1, 4, 3])
        8
        >>> somaListaInt([0])
        0
    '''

    soma: int = 0
    for i in numeros:
        soma = soma + i
    return soma
    
def somaListaReal(numeros: list[float]) -> float:
    '''Soma todos os valores de uma lista e retorna o valor.
    
        Exemplos:
        >>> somaListaFloat([50.2, 50, 50, 50, 50])
        250.2
        >>> somaListaFloat([0])
        0
    '''
    
    soma: float = 0
    for i in numeros:
        soma = soma + i
    return soma

def totaliza_pedidos(totalizacao: list[Totalizacao]) -> Pedido:
    '''Produz uma estrutura que totaliza a demanda de cada produto
        a partir de pedidos.

        Exemplos:
        >>> totaliza_pedidos([Totalizacao(tipo=TipoProduto.BOBINA, quantidade=12, qtdDesconto=10, precoCusto=50.0, total=212.4, lucro=10.0, porcDesconto=12), [Totalizacao(tipo=TipoProduto.BOBINA, quantidade=5, qtdDesconto=10, precoCusto=50.0, total=300.0, lucro=10.0, porcDesconto=12), [Totalizacao(tipo=TipoProduto.BOBINA, quantidade=20, qtdDesconto=10, precoCusto=50.0, total=1056.0, lucro=10.0, porcDesconto=12), [Totalizacao(tipo=TipoProduto.CHAPA, quantidade=2, qtdDesconto=8, precoCusto=40.0, total=96.0, lucro=8.0, porcDesconto=8.0), [Totalizacao(tipo=TipoProduto.CHAPA, quantidade=3, qtdDesconto=8, precoCusto=40.0, total=114.0, lucro=8.0, porcDesconto=8.0), [Totalizacao(tipo=TipoProduto.CHAPA, quantidade=4, qtdDesconto=8, precoCusto=40.0, total=192.0, lucro=8.0, porcDesconto=8.0), [Totalizacao(tipo=TipoProduto.PAINEL, quantidade=50, qtdDesconto=10, precoCusto=75.0, total=3825.0, lucro=15.0, porcDesconto=15.0)]    
        Pedido([Totalizacao(tipo=TipoProduto.BOBINA, quantidade=37, qtdDesconto=10, precoCusto=50.0, total=212.4, lucro=10.0, porcDesconto=12), Totalizacao(tipo=TipoProduto.CHAPA, quantidade=9, qtdDesconto=8, precoCusto=397.44, total=96.0, lucro=8.0, porcDesconto=8.0), Totalizacao(tipo=TipoProduto.PAINEL, quantidade=50, qtdDesconto=10, precoCusto=75.0, total=3825.0, lucro=15.0, porcDesconto=15.0)], 4133.4, 'José Louro', 'Maria Moreno')
        >>> totaliza_pedidos([]) is None
        True
    '''

    if len(totalizacao) > 0:
        i: int = 0
        pedido: Pedido = Pedido([Totalizacao(tipo=TipoProduto.BOBINA, quantidade=0, qtdDesconto=10, precoCusto=50.0, total=0, lucro=10.0, porcDesconto=12), Totalizacao(tipo=TipoProduto.CHAPA, quantidade=0, qtdDesconto=8, precoCusto=397.44, total=0, lucro=8.0, porcDesconto=8.0), Totalizacao(tipo=TipoProduto.PAINEL, quantidade=0, qtdDesconto=10, precoCusto=75.0, total=0, lucro=15.0, porcDesconto=15.0)], 0, '', '')

        # Busca quais são os tipos de produtos da lista de totalização
        if i < len(pedido.produtos) - 1:
            while i < len(totalizacao):
                if len(pedido.produtos) > 1 and totalizacao[i].tipo == totalizacao[i + 1].tipo:
                # Calcula a quantidade de cada produto
                    pedido.produtos[i].quantidade = pedido.produtos[i].quantidade + pedido.produtos[i + 1].quantidade
                # Calcula o valor total de cada produto
                    pedido.produtos[i].total = pedido.produtos[i].total + pedido.produtos[i].total
                i = i + 1
        
    else:
        return None


def ha_ruptura(estoque: Totalizacao, demanda: Totalizacao) -> list[TipoProduto]:
    '''Gera a partir do estoque e demanda, uma lista com os tipos de produtos
        com ruptura do estoque.
    '''

if __name__ == "__main__":
    import doctest
    doctest.testmod()