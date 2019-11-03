def jogar():
    print("**********************************************")
    print("******                                ********")
    print("******  Bem vindo ao jogo da Forca!   ********")
    print("******                                ********")
    print("**********************************************")
    def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if(erros == 7):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(erros == 6):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(erros == 2):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    def loser1():
        print("VOCÊ FRACASSOU!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def wiin():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    palavra_secreta = "amora".upper()
    palavra_final = ["_" for letra in palavra_secreta]
    acertou = False
    enforcou = False
    tentativas = 7

    while(not acertou and not enforcou):
        print(palavra_final)
        chute = input("Escolha uma letra")
        chute = chute.strip().upper()
        i = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if(chute == letra):
                    palavra_final[i] = letra
                i = i + 1
            print(palavra_final)
        else:
            desenha_forca(tentativas)
            tentativas -=1
        acertou = "_" not in palavra_final
        enforcou = tentativas == 0

    if acertou:
        wiin()
    else:
        loser1()
    print("Fim do Jogo")
    
if(__name__ == "__main__"):
    jogar()
        
