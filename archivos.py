
# manejo de archivos con "r" donde read es para leer
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


# manejo de archivos con "w" donde write es para escribir(sobrescribe el archivo)
def write():
    names = ["Juan", "Pedro", "Maria", "Carlos"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")


# manejo de archivos con "a" donde append es para agregar al final del archivo
def write2():
    names = ["Juan", "Pedro", "Maria", "Carlos"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")


def run():
    read()
    write()


if __name__ == '__main__':
    run()
