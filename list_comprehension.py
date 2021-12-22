def run():
    square = [i ** 2 for i in range(1, 101) if i % 3 != 0]

    # for i in range(1, 101):
    #     if not i % 3 == 0:
    #         square.append(i**2)
    print("----------------------------------")
    print("Cien primeros numeros naturales...")
    print("----------------------------------")
    print(square)
    print("\n")

    reto1 = [i for i in range(1, 10000) if i %
             4 == 0 and i % 6 == 0 and i % 9 == 0]
    print("--------------------------------------------")
    print("Reto1 Numeros que son multiplos de 4, 6 y 9")
    print("--------------------------------------------")
    print(reto1)
    print("\n")


if __name__ == '__main__':
    run()
