import random


def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo de FORCA! **")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras)) #escolher a palavra aleatóriamente
    palavra_secreta = palavras[numero].upper() #letra maiuscula, para não diferenciar

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? :  ")
        chute = chute.strip().upper() #strip - tirar os espaços

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra #adiciona as letras corretas na lista
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(erros == 1):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")

        if (erros == 2):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|       |  ")
            print("|       |  ")

        if (erros == 3):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|      /|  ")
            print("|       |  ")

        if (erros == 3):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|      /|  ")
            print("|       |  ")

        if (erros == 4):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|      /|\ ")
            print("|       |  ")

        if (erros == 4):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|      /|\ ")
            print("|       |  ")

        if (erros == 5):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|      /|\ ")
            print("|       |  ")
            print("|      /   ")

        if (erros == 6):
            print(" _______   ")
            print("|/      |  ")
            print("|      (_) ")
            print("|      /|\ ")
            print("|       |  ")
            print("|      / \  ")




    if (acertou):
        print("### VOCE GANHOU! ###")
    else:
        print("@@@ VOCE PERDEU, TENTE NOVAMENTE! a palavra era {} @@@".format(palavra_secreta))

    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()



