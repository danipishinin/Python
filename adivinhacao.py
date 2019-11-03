import random
def jogar():
    print("**************************************************")
    print("******                                    ********")
    print("******  Bem vindo ao jogo de Adivinhação! ********")
    print("******                                    ********")
    print("**************************************************")

    pontuacao = 1000
    tentativa = 1
    numero_secreto = random.randrange(1,101)
    print(numero_secreto,"SPOILERS!!!!!!!!!!!!")

    nivel = int(input("Escolha o nível de dificuldade {1} Fácil | {2} Médio | {3} Difícil"))
    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for tentativa in range(1,total_de_tentativas + 1):

        print("Tentativa {}".format(tentativa))
        chute = int(input("Digite um número entre 1 e 100: "))
            
        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if(acertou):
            print("VOCE GANHOU 1 MILHAO DE NADAS!!!!")
            break
        else:
            if(maior):
                print("VOCE DIGITOU UM NUMERO MAIOR QUE O NUMERO SECRETO.")
                pontuacao = pontuacao - abs(numero_secreto - chute)
            elif(menor):
                print("VOCE DIGITOU UM NUMERO MENOR QUE O NUMERO SECRETO.")
                pontuacao = pontuacao - abs(numero_secreto - chute)

        tentativa = tentativa + 1
        total_de_tentativas = total_de_tentativas + 1
    print("FIM DO JOGO!!! Sua Pontuação Foi {}".format(pontuacao))

if(__name__ == "__main__"):
    jogar()
