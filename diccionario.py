# import ascii_magic

# salida = ascii_magic.from_image_file(
#     'ahorcado.jpg', columns=80, char="*")

# ascii_magic.to_terminal(salida)

especial = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú"}
especial2 = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}

palabra = "éstálló"


for i, letra in enumerate(palabra):
    if letra in especial2:
        print(especial2.get(letra))

    pass
