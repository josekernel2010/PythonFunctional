# funcion donde se ingresa un numero y se va agregando a la lista divisor
# los numeros que son divisores de 1 hasta el numero ingresado
def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


# Manejando errores con try y except donde devuelve un mensaje de error y la funcion
# para repetir el proceso
def run():
    try:
        num = int(input('Ingrese un numero: '))
        print(divisor(num))
    except ValueError:
        print('Error, debe ingresar un numero')
        return run()


# Raise me envia un error y except me permite capturar el error
def raise1():
    try:
        palabra = input('Ingrese una palabra: ')
        if len(palabra) == 0:
            print('Error...')
            raise ValueError(':: Espacio vacio error raise ::')
        if palabra == palabra[::-1]:
            print('Es palindromo')
        else:
            print('No es palindromo')
    except ValueError as e:
        print(e)


# Finally siempre se ejecuta
def funcion_final():
    try:
        num = int(input('Ingrese un numero: '))
        print(divisor(num))
    except ValueError:
        print('Error, debe ingresar un numero')
    finally:
        print('Finally siempre se ejecuta...')


# funcion principal
if __name__ == '__main__':

    # Manejando errores con try y except donde devuelve un mensaje de error y la funcion
    run()

    # Raise me envia un error y except me permite capturar el error
    raise1()

    # Finally siempre se ejecuta
    # sirve para cuando se trabaja con archivos y se necesita cerrar el archivo
    funcion_final()
