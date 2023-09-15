# Resolvendo exercícios práticos


#%%
""" Crie um programa que sorteia, aleatoriamente, um número inteiro menor que 100. """
from random import randrange

numero_escolhido = randrange(100)
print(numero_escolhido)
#---------------------------------------------------------------------------
# %%
"""  Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º. """
from math import pow

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
resultado = pow(numero_1, numero_2)

print(f"Primeiro número é {numero_1}")
print(f"Segundo número é {numero_2}")
print(f"{numero_1} elevado a {numero_2} é: {resultado}")
#-----------------------------------------------------------------
# %%

"""Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes.
Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado."""

from random import sample

num_participantes = int(input("Forneça o número de participantes: "))

lista = []
for i in range (1,num_participantes + 1):
    lista.append(i)

escolhido = sample(lista, 1)[0] # escolhe um número da lista

print(lista)
print(f"O participante escolhido é o de número {escolhido}")
#----------------------------------------------------------------------------------------------------------------------
# %%

""" Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. 
O token precisa ser par e variar de 1000 até 9998.Escreva um código que solicita à pessoa usuária o seu nome
e exibe uma mensagem junto a esse token gerado aleatoriamente."""

from random import randint

nome = input("Entre com seu nome: ")
token = randint(1000, 9998)
print(f"Olá, {nome}, seu token de acesso é {token}. Seja bem-vindo(a)!")

# %%
