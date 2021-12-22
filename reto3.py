def run():
    reto3 = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print("-----------------------------------------------------------------------------------------------")
    print("Reto3 Diccionario con los primeros 100 numeros cubiertos por su cubo y que no son multiplo de 3")
    print("-----------------------------------------------------------------------------------------------")
    print(reto3)
    print("\n")


if __name__ == '__main__':
    run()
