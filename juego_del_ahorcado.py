from os import system
# libreria para manejar el titulo y dar formato al texto
import pyfiglet
'''
autor: @jose_mateo_2010

'''
draw = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# funcion que lee un archivo y devuelve una palabra con la libreria random (1)
def archivo():
    with open("./archivos/data.txt", "r", encoding='utf-8') as f:
        lista = [line1 for line1 in f if line1.strip()]
    from random import choice
    palabra = choice(lista)
    return palabra


# Funcion que muestra el juego (2)
def proceso(titulo, palabra, palabra2, cont, caja, especial):
    while True:
        system("cls")
        print(titulo)
        print("---------------")
        print(palabra)
        print("---------------")
        print(draw[cont])
        print(len(palabra)*"**")
        # utilizo join para unir la lista en un string
        print(" ".join(palabra2))
        print()
        print(len(palabra)*"**")
        

        # manejo de errores
        try:
            letter = input("Ingrese una letra: ")

            for l, v in enumerate(palabra):
                # compara la letra ingresada con la letra de la palabra
                if letter == v:
                    palabra2[l] = letter
                # si la letra se encuentra en el diccionario especial y letra ingresada es igual a la letra del diccionario
                # se reemplaza la letra ingresada por la letra del diccionario
                if v in especial and letter == especial.get(v):
                    palabra2[l] = v

            # si la palabra2 es igual a palabra, se cumple la condicion de ganar
            if "".join(palabra2) == palabra:
                system("cls")
                print(draw[cont])
                ganar = pyfiglet.figlet_format("GANASTE...")
                print(ganar)
                print("---------------")
                print("Ganaste 😄😄 !!!")
                print("Palabra: "+" ".join(palabra2))
                print("---------------")
                break

            # si la letra ingresada no se encuentra en la palabra o está em la caja de letras ya ingresadas
            if letter not in palabra or letter in caja or letter == "":
                cont += 1
                if cont == 6:
                    system("cls")
                    print(draw[cont])
                    perdiste = pyfiglet.figlet_format("PERDISTE...")
                    print(perdiste)
                    print("--------------------")
                    print("Perdiste  😱😱 !!!")
                    print("Palabra: "+palabra)
                    print("--------------------")
                    break
            caja.add(letter)

            # con assert creo el error si letter no es una letra
            assert letter.isalpha(), ":: Error ingrese una letra"

        # aviso del error
        except AssertionError as e:
            system("cls")
            print(titulo)
            print("---------------")
            print(palabra)
            print("---------------")
            print(draw[cont])
            print("---------------------------")
            print(e)
            print("---------------------------")
            input("Presione enter para continuar...")


# funcion que prepara el arranque del juego (3)
def hangman():
    # para quitar los espacios en blanco a principio y final del string
    palabra = archivo().strip()
    # doy como separación un espacio en blanco despues del guión bajo para que la lista no sea de un solo elemento
    palabra2 = (len(palabra) * "_ ")
    # convierto a plabra2 en una lista para poder modificarla por medio de indices
    palabra2 = palabra2.split()
    cont = 0
    caja = set()
    # utilizo el diccionario para manejar las letras con tilde
    especial = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    titulo = pyfiglet.figlet_format("HANGMAN")

    proceso(titulo, palabra, palabra2, cont, caja, especial)


# funcion principal
def run():
    hangman()


if __name__ == '__main__':
    run()
