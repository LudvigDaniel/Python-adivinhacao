def jogar():

    import random


    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_aleatorio = random.randrange(0,101) 
    numero_secreto = round(numero_aleatorio)
    total_de_tentativas = 0
    pontos = 1000
    print(numero_secreto) ##Teste 

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível:   "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5    


    for rodada in range(1, total_de_tentativas +1 ): 
        print("Tentativa {} de {}.".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100:   ")
        print("Você digitou " , chute_str )
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        erro = rodada >= total_de_tentativas

        if (acertou):
            print("*********************")
            print("*** Você Acertou! ***")
            print("**********{}*********" .format(pontos))
            print("***** Parabéns! *****")
            print("*********************")
            print("*****Fim do Jogo*****")
            print("*********************")
            break

        else:
            if(maior): 
                print("Você errou! O seu chute foi MAIOR do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi MENOR do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos


    if(erro):       
        print("**********************")
        print("Fim do Jogo, Perdedor!")
        print("**********************")
        print("O número secreto era {} " .format(numero_secreto))


if(__name__ == "__main__"):
    escolhe()