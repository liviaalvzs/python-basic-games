import random


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r") 
    palavras = [] 

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]
    
def solicita_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    
def revela_letra(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_sucesso():
    print("Você ganhou")

def mensagem_fracasso():
    print("Você perdeu")

def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = solicita_chute()
        if(chute in palavra_secreta):
            revela_letra(palavra_secreta, chute, letras_acertadas)   
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        mensagem_sucesso()
    else:
        mensagem_fracasso()
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
