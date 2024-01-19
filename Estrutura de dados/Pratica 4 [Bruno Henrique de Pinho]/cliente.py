import random

class Cliente():
    ''' Modela um cliente '''

    @classmethod
    def geraCliente(cls, probDeNovosClientes,
                         tempoDeChegada,
                         tempoGastoPorCliente):
        ''' Tenta gerar um cliente de acordo com probDeNovosClientes '''
        # Random.random ->> Retorna um ponto flutuante entre 0 e 1
        if random.random() <= probDeNovosClientes:
            return Cliente(tempoDeChegada, tempoGastoPorCliente)
        else:
            return None
       
    def __init__(self, tempoDeChegada, qtdDeAtendimentoNecessario):
        ''' Inicializa um cliente '''
        self.tempoDeChegada = tempoDeChegada
        self.qtdDeAtendimentoNecessario = qtdDeAtendimentoNecessario

    def retornaTempoDeChegada(self):
        return self.tempoDeChegada
   
    def retornaQtdDeAtendimentoNecessario(self):
        return self.qtdDeAtendimentoNecessario
   
    def atenda(self):
        ''' Aceita uma unidade de atendimento do caixa '''
        self.qtdDeAtendimentoNecessario -= 1
