
def run():
    my_list = [1, "hello", 4.5, True]
    my_dict = {"firstname": "Icaro", "lastname": "De Creta"}

    super_list = [
        {"firstname": "Icaro", "lastname": "De Creta"},
        {"firstname": "Venus", "lastname": "De Nilo"},
        {"firstname": "Afrodita", "lastname": "Del Olimpo"},
        {"firstname": "Sofia", "lastname": "Medichi"},
        {"firstname": "Anastasia", "lastname": "Montiel"},
        {"firstname": "Cesar", "lastname": "Roma"},
        {"firstname": "Maria", "lastname": "Seller"}
    ]

    super_dict = {
        "natural_num": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "integer_num": [-1, -2, -3, 0, 1, 2, 3],
        "float_num": [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i.get("firstname"), "-", i.get("lastname"))


if __name__ == '__main__':
    run()
