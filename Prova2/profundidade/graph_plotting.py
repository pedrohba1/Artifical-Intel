import matplotlib.pyplot as plt
import pandas as pd




df =pd.read_csv('labirinto.csv')

print(df['movimentos'].mean())
print(df['passos'].mean())

#plt.boxplot(df.movimentos)
plt.boxplot(df.passos)

plt.show()