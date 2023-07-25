import forca
import adivinhacao

print("\n******************************")
print("Escolha um jogo para jogar")
print("******************************")


sair = False

while (not sair):

    print("\nMENU DE JOGOS")
    print("(1) Forca (2) Adivinhacao (3) Sair")
    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhacao")
        adivinhacao.jogar()
    elif (jogo == 3):
        sair = True

print("Obrigado por jogar!")
