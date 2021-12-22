# operador ternario

var = 10
ternario = 'mayor' if var > 5 else 'menor'
print("")
print("--------------------------")
print("Operador ternario:", ternario)


# funciones lambda
# palindromo = lambda cadena: cadena == cadena[::-1]
def palindromo(cadena): return cadena == cadena[::-1]


print("--------------------------")
print("Si la funcion es palindromo:", palindromo("hola"))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter para filtrar una lista
impares = list(filter(lambda x: x % 2 != 0, lista))
print("--------------------------")
print("Aplicando filter:")
print("Impares:", impares)

# map recorre toda la lista y devuelve una nueva lista
print("--------------------------")
print("Aplicando map:")
cubico = list(map(lambda x: x ** 3, lista))
print("Cubicos:", cubico)
print("--------------------------")

# reduce reduce una lista a un valor unico, hay que importar la libreria functools
from functools import reduce

print("--------------------------")
sumatoria = reduce(lambda x, y: x + y, lista)
print("Sumatoria:", sumatoria)
