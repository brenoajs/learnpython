# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.


cities = {

    'recife': {
        'country': 'brazil',
        'population': '1.555 milhão',
        'fact': 'é conhecida como cidade das pontes',
    },

    'nova york': {
        'country': 'EUA',
        'population': '19.59 milhões',
        'fact': 'é conhecida como uma das maiores megalopoles do mundo',
    },

    'São Paulo': {
        'country': 'brazil',
        'population': '12.18 milhões',
        'fact': 'é conhecida como cidade cinza',
    },

}

for cidade, valores in cities.items():
    print(f"Aqui vão algumas informações importantes sobre {cidade.title()}:")
    for valor in valores:
        print(f"{valor.title()}: {valores[valor].title()}")
    print("\n")


