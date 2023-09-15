#%%
import matplotlib
import matplotlib.pyplot as plt


estudantes = ["João", "maria", "Fernando"]
notas = [10, 8, 9.5]

#criando um grafico de barras
plt.bar(x = estudantes, height = notas)

#%%

from random import choice
estudantes_2 = ["João", "maria", "Fernando", 'Ana']
estudante = choice(estudantes_2) # escolhendo um estudante aleatório
#------------------------------------------------------------------------------------------------------------------------------------------
# %%
from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

resultado = sample(lista, 5) # escolhe 5 números aleatórios de lista e adiciona em uma nova lista
print(lista,f"\n{resultado}")
#------------------------------------------------------------------------------------------------------------------------------------------
# %%
# Função lambda

nota = 8
qualitativo = lambda x: x + 0.5
nota_final = qualitativo(nota)
print(nota_final)
#------------------------------------------------------------------------------------------------------------------------------------------

# %%
temp_celsius = [0,25,37,78,100]
temp_fahrenheit = list(map(lambda x: x* 9/5 + 32, temp_celsius)) 
temp_fahrenheit
#------------------------------------------------------------------------------------------------------------------------------------------