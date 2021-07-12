def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "livro"
    letras_acertadas = ["_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    tentativas = 0
    index = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            tentativas += 1
        
        enforcou = tentativas == 6

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
