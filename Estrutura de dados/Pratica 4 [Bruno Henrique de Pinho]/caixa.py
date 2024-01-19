from dataclasses import dataclass
from fila import FilaEstatica
from cliente import Cliente

@dataclass
class Item:
    ''' Representa um item da fila do simuladorDeFilas '''
    valor: Cliente


class Caixa():
    ''' Modela um caixa '''

    def __init__(self):
        ''' Inicializa o caixa '''
        self.tempoDeEsperaTotal = 0
        self.clientesAtendidos = 0
        self.clienteAtual = None
        self.filaDeClientes = FilaEstatica(50)

    def adicionaCliente(self, c):
        ''' Adiciona um cliente a fila '''
        self.filaDeClientes.enfileira(Item(c))
   
    def atendeClientes(self, tempoAtual):
        ''' Atende um cliente durante uma unidade de tempo '''
        if self.clienteAtual is None:
            # Sem clientes ainda
            if self.filaDeClientes.vazia():
                return
            else:
                # Desenfileire o primeiro cliente 
                self.clienteAtual = self.filaDeClientes.desenfileira().valor
                self.tempoDeEsperaTotal += (tempoAtual - self.clienteAtual.retornaTempoDeChegada())
                self.clientesAtendidos += 1

        # Atenda o cliente atual
        self.clienteAtual.atenda()

        # Se o atendimento do cliente atual terminou, descarte-o   
        if self.clienteAtual.retornaQtdDeAtendimentoNecessario() == 0:
            self.clienteAtual = None
   
    def __str__(self):
        ''' Retorna os dados do caixa como uma string '''
        if self.clientesAtendidos != 0:
            tempoMedio = float(self.tempoDeEsperaTotal) / self.clientesAtendidos
        else:
            tempoMedio = 0.0
            
        resultado = 'Clientes atendidos: %16d\nTempo médio de espera: %16.2f\nClientes restantes na fila: %8d'\
                     % (self.clientesAtendidos, 
                        tempoMedio,
                        self.filaDeClientes.tamanho())
        return resultado
