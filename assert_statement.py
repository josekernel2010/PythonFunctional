
# Assert statement es una afirmacion de un error tipo AssertionError
def run():
    num = int(input("Enter a number: "))
    assert num > 0, "Number must be greater than zero"
    print("Thank you")


# Funcion con try except que atrapa el error AssertionError
def try_assert():
    try:
        run()
    except AssertionError as err:
        print(err)


# Funcion recursiva con la aplicacion correcta para verificar si el input es un numero
def prueba():
    num = input("Enter a number: ")
    if num.isnumeric() == False:
        print("Please enter a number")
        prueba()
    else:
        print("Thank you")


if __name__ == '__main__':

    # probando la funcion con assert
    run()

    # probando la funcion con try except y assert
    try_assert()

    # probando la funcion con recursividad y el correcto uso de la funcion isnumeric()
    prueba()
