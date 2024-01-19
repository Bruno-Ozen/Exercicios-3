from dataclasses import dataclass
from copy import deepcopy
from fila import FilaEstatica
from fila import Item

fila_clientes_p = FilaEstatica(50)
fila_clientes_c = FilaEstatica(50)
contador_fila_p = [1]
contador_fila_c = [1]
sequencia_caixas = []

@dataclass
class Caixa():
    numero: int
    cliente_at: str

def gerar_caixas(quantidade: int):
    for c in range(1, quantidade+1):
        cx = Caixa(c,'Livre')
        sequencia_caixas.append(cx)

def status_caixas():
    for caixa in range(len(sequencia_caixas)):
        print('Caixa:',sequencia_caixas[caixa].numero,'Atendimento:',sequencia_caixas[caixa].cliente_at)

def libera_caixas():
    for caixa in range(len(sequencia_caixas)):
        sequencia_caixas[caixa].cliente_at = 'Livre'

def status_fila():
    print('Prioritária:')
    fila_clientes_p.exibe()
    print('Comum:')
    fila_clientes_c.exibe()

def gerar_senha():
    print('Selecione o tipo de atendimento: 1 - Prioriário, 2 - Comum')
    tipo = int(input('tipo: '))

    if tipo == 1:
        if fila_clientes_p.cheia():
            print('Fila Prioritária cheia, aguarde...')
        else:
            senha = Item('P'+str(deepcopy(contador_fila_p[0])))
            fila_clientes_p.enfileira(senha)
            contador_fila_p[0] += 1
            print('Senha gerada:', senha.valor)
    elif tipo == 2:
        if fila_clientes_c.cheia():
            print('Fila Comum cheia, aguarde...')
        else:
            senha = Item('C'+str(deepcopy(contador_fila_c[0])))
            fila_clientes_c.enfileira(senha)
            contador_fila_c[0] += 1
            print('Senha gerada:', senha.valor)

def chama_cliente():
    if fila_clientes_p.vazia() and fila_clientes_c.vazia() is True:
        libera_caixas()
        print('Não há clientes nas filas...')
    elif fila_clientes_p.vazia() is False:
        num_cx = int(input('informe o número do caixa: '))
        if (num_cx - 1) < 0 or num_cx > len(sequencia_caixas):
            print('O número digitado está fora do intervalo de caixas')
        else:
            cl_atendido = deepcopy(fila_clientes_p.desenfileira().valor)
            sequencia_caixas[(num_cx)-1].cliente_at = cl_atendido
            print('Senha:', cl_atendido,'Diriga-se ao caixa:', num_cx)
    elif fila_clientes_c.vazia() is False:
        num_cx = int(input('informe o número do caixa: '))
        if (num_cx - 1) < 0 or num_cx > len(sequencia_caixas):
            print('O número digitado está fora do intervalo de caixas')
        else:
            cl_atendido = deepcopy(fila_clientes_c.desenfileira().valor)
            sequencia_caixas[(num_cx)-1].cliente_at = cl_atendido
            print('Senha:', cl_atendido,'Diriga-se ao caixa:', num_cx)

def main() -> None:
    numero_caixas = int(input('Informe o número de caixas para atendimento, informar valores maiores ou igual a 2 e menor ou igual a 20:'))
    if numero_caixas < 2 or numero_caixas > 20:
        print('Valor não permitido, aplicação encerrada')
    else:
        gerar_caixas(numero_caixas)
        saida_aplicacao = 0
        while saida_aplicacao != 5:
            print('\n Menu de ações:')
            print('1 - Gerar senha')
            print('2 - Chamar cliente')
            print('3 - Consultar clientes em espera')
            print('4 - Consultar estados dos caixas')
            print('5 - Sair da aplicação \n')
            opcao = int(input())
            if opcao == 1:
                gerar_senha()
            elif opcao == 2:
                chama_cliente()
            elif opcao == 3:
                status_fila()
            elif opcao == 4:
                status_caixas()
            elif opcao == 5:
                saida_aplicacao = 5

if __name__ == "__main__":
    main()