
# Funcion que devuelve los divisores de un numero
def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


# Funcion con assert y try para atrapar errores dentro de una funcion recursiva
def num_negative():
    try:
        num = int(input("Ingrese un numero: "))
        assert num > 0, "error numero menor que cero"
        d = divisor(num)
        print(d)
    except ValueError:
        print("Error, no es un numero")
        num_negative()


if __name__ == '__main__':

    num_negative()
