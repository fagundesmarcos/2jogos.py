import forca
import adivinhacao

def escolha_jogo():

    print("*********************************")
    print("******** Escolha o jogo *********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? :"))

    if(jogo == 1):
        print("jogando Forca!")
        forca.jogar()
    elif(jogo == 2):
        print("jogando Adivinhação!")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolha_jogo()