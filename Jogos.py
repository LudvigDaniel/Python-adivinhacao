import forca
import adivinhacao

def escolhe():
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************")

    print("(1) Forca ; (2) Adivininhação")

    jogo = int(input("Qual Jogo?"))

    if(jogo == 1):
        print("jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe()
