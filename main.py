import random


def jogar():
    mensagem_abertura()
    palavra_secreta = busca_palavra_secreta()
    letras_acertadas = campo_letras(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = chute_jogador()

        if chute in palavra_secreta:
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        ganhou()
    else:
        perdeu(palavra_secreta)


def mensagem_abertura():
    print("***********************************")
    print("****Bem vindo ao jogo da forca!****")
    print("***********************************")


def busca_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def campo_letras(palavra_secreta):
    lista = ["_" for _ in palavra_secreta]
    return lista


def chute_jogador():
    chute = input("Qual a letra?")
    chute = chute.strip().upper()
    return chute


def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def ganhou():
    print("****** Parabéns!!! ******")
    print("Você é muito inteligente!!!")
    print("Ficamos felizes por sua vitória!!!")
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
    print("*************************")


def perdeu(palavra_secreta):
    print("***** você perdeu!! *****")
    print("A palavra secreta era {} ".format(palavra_secreta))
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |     ")
        print(" |           ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
