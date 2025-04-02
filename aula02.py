import matplotlib.pyplot as plt

# Importa a biblioteca pandas
import pandas as pd

def exibirGrafico():
    #cria o dataframe
    df = pd.DataFrame({
        "Meses": ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'],
        "Temperaturas": [29,31,30,28,27,25,21,24,27,28,29,33]
    })

    #Redimensionando o gráfico
    plt.figure(figsize=[10.0, 5.0])

    #Criação de gráfico
    plt.plot(df['Meses'], df['Temperaturas'], color="purple")

    #Definição dos títulos
    plt.title("temperatura média ao longo do tempo")
    plt.xlabel("Meses")
    plt.ylabel("Temperatura")

    # Exibindo o grafico
    plt.show()
    plt.savefig('chart2.png')

    #exibe no console dados estatisticos
    print(f'Temperaturas: \n{df['Temperaturas'].describe()}')
