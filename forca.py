def jogar():
    print("****************************")
    print("Esse é o jogo da forca :)!")
    print("****************************")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    #enquanto (True) continua jogando
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
              print("Encontre a letra {} na posição {}".format(letra, index))
        index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
