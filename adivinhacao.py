import random


def jogar():

    print("\n******************************")
    print("Bem vindo ao jogo de adivinhação")
    print("******************************")

    # gerar um número aleatório de 1 a 100
    numero_secreto = random.randrange(1, 101)
    print("\nTente adivinhar o número secreto")

    print("\nQual nível de dificuldade deseja jogar?", numero_secreto)
    print("(1) Fácil, (2) Médio ou (3) Difícil")

    nivel = int(input("Defina o nível: "))

    # tentativas por nível
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    pontos = 1000

    # loop das condições
    for rodada in range(1, total_de_tentativas + 1):

        print("\nTentativas restantes {}".format(
            total_de_tentativas - rodada + 1))
        print("caso deseje sair, digite 500")
        chute = input("\nDigite o seu numero: ")
        # transforma a entrada de input em um número inteiro
        chute = int(chute)

        # Condições
        acertou = chute == numero_secreto
        maior = chute > numero_secreto+10
        menor = chute < numero_secreto-10
        quase_menos = numero_secreto - 10 <= chute < numero_secreto
        quase_mais = numero_secreto < chute <= numero_secreto + 10
        quer_sair = chute == 500

        if (acertou):
            print("Voce ACERTOU !!!!!!")
            break  # sai do laço while caso a pessoa acerte o número secreto
        else:
            if (quer_sair):
                print("\nQuis sair do jogo")
                break
            elif (maior):
                print("\nSeu chute foi muito alto. Tente um número menor")
            elif (menor):
                print("\nSeu chute foi muito baixo. Tente um número maior")
            elif (quase_menos):
                print(
                    "\nSeu chute ({:02.0F}) foi menor que o número secreto, porém perto. Tente novamente".format(chute))
            elif (quase_mais):
                print(
                    "\nSeu chute ({:02.0F}) foi maior que o número secreto, porém perto. Tente novamente".format(chute))

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Pontos finais {}\nFim de Jogo".format(pontos))


if (__name__ == "__main__"):
    jogar()
