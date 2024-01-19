from caixa import Caixa
from cliente import Cliente

# Aluno: Bruno Henrique de Pinho
# RA: 133301

class SimuladorDeFila():
    ''' Modela um simulador de uma fila de caixa '''

    def __init__(self, tempoDeSimulacao, tempoGastoPorCliente,
                 probDeNovosClientes):
        ''' Inicializa o simulador '''
        self.probDeNovosClientes = probDeNovosClientes
        self.tempoDeSimulacao = tempoDeSimulacao
        self.tempoGastoPorCliente = tempoGastoPorCliente
        self.caixa = Caixa()
   
    def executaSimulador(self):
        ''' Executa o simulador pelo tempoDeSimulacao '''
        for tempoAtual in range(self.tempoDeSimulacao):
            # Tente gerar um novo cliente
            cliente = Cliente.geraCliente(
                self.probDeNovosClientes,
                tempoAtual,
                self.tempoGastoPorCliente)

            # Se o cliente foi gerado, inclua-o na fila do caixa
            if cliente != None:
                self.caixa.adicionaCliente(cliente)

            # Faça o caixa atender um cliente
            self.caixa.atendeClientes(tempoAtual)

    def imprimeResultado(self):
        ''' Retorna os resultados da simulação '''
        print(str(self.caixa))


def main() -> None:
    ''' 
    **** Função principal ****
    Ela deve:
     - ler os dados de entrada; 
     - criar um SimuladorDeFila;
     - executar a simulação;
     - imprimir o resultado
     '''
    tempoSimulacao = int(input('Digite o tempo de simulação: '))
    tempoGastoPorCliente = int(input('Digite o tempo gasto por cliente: '))
    probDeNovosClientes = float(input('Digite a probabilidade de novos clientes: ')) / 100
    simulador = SimuladorDeFila(tempoSimulacao, tempoGastoPorCliente, probDeNovosClientes)
    simulador.executaSimulador()
    simulador.imprimeResultado()

if __name__ == "__main__":
    main()