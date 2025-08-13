import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de dados exemplo
dados = [120, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

# Calcular quartis
quartis = np.percentile(dados, [25,50,75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')


# Visualização por BoxPlot
plt.boxplot(dados, vert=False)
plt.title('boxplot das vendas')
plt.xlabel('vendas')
plt.show()
plt.savefig('chartrecuperacao.png')