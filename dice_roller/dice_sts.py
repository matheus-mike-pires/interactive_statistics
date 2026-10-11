import random
import numpy as np
import matplotlib.pyplot as plt
import stats as st
import pandas as pd

contador = 0
lista_dados = []
n_total=int(input('Enter the number of rolls: '))

while contador < n_total:
    dado_rolagem = random.randint(1, 6)
    lista_dados.append(dado_rolagem)
    contador += 1

print('Random dice display - Statistical analysis of a 6-sided die \n')
print('Number of rolls:', len(lista_dados))
print('Median:', np.median(lista_dados))
print('Mean:', np.mean(lista_dados))
try:
    print('Mode:', st.mode(lista_dados))
except:
    print('Mode: No mode found')

print('\n')
agrupado = pd.Series(lista_dados).value_counts().sort_index()
print('Frequency of each outcome:')
print(agrupado)

plt.figure(figsize=(8, 6))
plt.suptitle('Random Dice Display - Statistical Analysis of a 6-Sided Die', fontsize=16)
plt.subplot(1, 2, 1)
agrupado.plot.pie(color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
plt.xlabel('Dice results')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.subplot(1, 2, 2)
agrupado.plot.bar(color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
plt.xlabel('Dice results')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()
