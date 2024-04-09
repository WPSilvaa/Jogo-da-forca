
import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "forca", "divertido"]
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_incorretas = []
    tentativas_maximas = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem", len(palavra), "letras.")

    while True:
        print("\nPalavra: ", mostrar_palavra_oculta(palavra, letras_corretas))
        print("Letras corretas:", letras_corretas)
        print("Letras erradas:", letras_incorretas)

        palpite = input("Digite uma letra: ").lower()

        if palpite in palavra:
            letras_corretas.append(palpite)
            print("Correto!")
        else:
            letras_incorretas.append(palpite)
            print("Incorreto!")

        if len(letras_incorretas) == tentativas_maximas:
            print("Você perdeu! A palavra era:", palavra)
            break

        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns! Você venceu!")
            break

jogar_forca()
