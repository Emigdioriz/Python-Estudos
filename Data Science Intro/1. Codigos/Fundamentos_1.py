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
estudante = choice(estudantes_2) # escolhendo um estudantes aleatório


# %%
from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

resultado = sample(lista, 5)
print(lista,f"\n{resultado}")

# %%
