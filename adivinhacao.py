import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Define um nível: "))

    if(nivel == 1):
        total_de_tentativas = 15
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    #rodada = 1
    #while(rodada <= total_de_tentativas):

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("Voce digitou", chute)

        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("DIGITE UM NUMERO ENTRE 1 E 100")
            print("---------------------------------------------------")
            continue

        igual = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (igual):
            print("**********************")
            print("Voce acertou!! o numero escolhido foi o {}.".format(numero_secreto))
            print("Voce fez {} pontos!".format(pontos))
            print("**********************")
            break
        else:
            if (maior):
                print("Voce errou, chute um numero menor.")
                print("---------------------------------------------------")
            elif (menor):
                print("Voce errou, chute um numero maior.")
                print("---------------------------------------------------")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        #total_de_tentativas = total_de_tentativas - 1
        #rodada = rodada + 1


    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()
