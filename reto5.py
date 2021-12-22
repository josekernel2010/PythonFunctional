
def run():
    # filter funcion que filtra los datos de una lista
    dev_python = list(
        filter(lambda worked: worked['language'] == 'python', DATA))
    # map funcion que aplica una funcion a cada elemento de una lista
    dev_python = list(map(lambda worked: worked['name'], dev_python))
    # Filter para filtrar una lista
    all_platzi = list(
        filter(lambda worked: worked['organization'] == 'Platzi', DATA))
    # map para aplicar una funcion a cada elemento de una lista
    all_platzi = list(map(lambda worked: worked['name'], all_platzi))
    # function comprehension y "|" para unir diccionarios
    old_people = [worked | {'old': worked['age'] > 70} for worked in DATA]
    # comprenssion de listas para sacar los mayores de edad
    adults = [worked['name'] for worked in DATA if worked['age'] > 18]

    for worked in adults:
        print(worked)

    pass


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
