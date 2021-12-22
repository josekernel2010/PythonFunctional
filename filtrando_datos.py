
# Funcion de filtrado de datos
def run():
    # list comprehension crea una lista de nombres que cumplen con la condicion "python"
    dev_python = [work['name']for work in DATA if work['language'] == 'python']
    # list comprehension crea una lista de nombres que cumplen con la condicion "Platzi"
    workes_Platzi = [work['name']
                     for work in DATA if work['organization'] == 'Platzi']

    # filter funcion que filtra los datos de una lista
    mayor_de_edad = list(filter(lambda x: x['age'] > 18, DATA))
    # map funcion que aplica una funcion a cada elemento de una lista
    mayor_de_edad = list(map(lambda x: x['name'], mayor_de_edad))

    # el simbolo "|" de python 3.9 en adelante, es un operador de union entre diccionarios
    old_people = list(map(lambda x: x | {'old': x['age'] > 70}, DATA))

    for work in workes_Platzi:
        print(work)


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    }
]


if __name__ == '__main__':

    run()
