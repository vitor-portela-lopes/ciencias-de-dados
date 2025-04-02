# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
# Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def exibirGrafico():
    #definição dos grupos e valores
    grupos = ['A', 'B', 'C']
    valores = [23, 38, 12]

    # Configura o grafico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores
    plt.bar(grupos, valores, color=['red', 'blue', 'grey'])

    # Define o titulo do gráfico
    plt.title('Gráfico de barras Simples')

    # Define o título do eixo X
    plt.xlabel('Grupos')

    # Define o titulo do eixo y
    plt.ylabel('Valores')
    