import matplotlib.pyplot as plt
import pandas as pd




df =pd.read_csv('labirinto_2.csv')

print(df['movimentos'].mean())
print(df['caminho_total'].mean())
print(df['distancia_ao_final'].mean())


plt.boxplot(df.passos)

plt.show()