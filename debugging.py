
# funcion donde se ingresa un numero y se va agregando a la lista divisor
# los numeros que son divisores de 1 hasta el numero ingresado
def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor

# funcion donde ingreso un numero y se va agregando a la lista divisor
# despues esa lista se va a imprimir en pantalla


def run():
    num = int(input('Ingrese un numero: '))
    print(divisor(num))
    print("Programa terminado...")
    pass


# funcion principal
if __name__ == '__main__':
    run()
