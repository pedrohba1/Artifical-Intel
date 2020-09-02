import matplotlib.pyplot as plt
import pandas as pd




df =pd.read_csv('labirinto.csv')

print(df['movimentos'].mean())
print(df['passos'].mean())
print(df['distancia_ao_final'].mean())

#plt.boxplot(df.movimentos)
plt.boxplot(df.distancia_ao_final)

plt.show()