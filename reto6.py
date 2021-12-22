# manejo de error
def run():
    try:
        num = int(input("Ingrese un numero: "))

        if num < 0:
            # creando una excepcion
            raise TypeError("El numero ingresado es negativo")

        lista = []
        for i in range(1, num+1):
            lista.append(i**3)
        print("Lista de numeros elevados al cubo:\n", lista)
    # atrapando la excepcion que se genera "raise"
    except TypeError as e:
        print("-------------------------------------------")
        print("Error --> ", e)
        print("-------------------------------------------")


if __name__ == '__main__':

    try:
        run()
    except:
        print("------------------------")
        print("tipo de dato incorrecto")
        print("------------------------")
