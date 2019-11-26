#Exercício 6.8 do Python Crash Course.
#Feito em 25.11.2019
#Breno Jaruzo

pets = []

cookie = {
    'nome':'cookie',
    'dono':'carol',
    'idade': 3,
    'raça': 'shitzu',
}

pets.append(cookie)

negao = {
    'nome': 'negão',
    'dono': 'carla',
    'idade': 7,
    'raça': 'vira-lata',
}
pets.append(negao)

breno = {
    'nome': 'breno',
    'dono': 'carol',
    'idade': 28,
    'raça': 'humano',
}

pets.append(breno)

for pet in pets:
    print(f"O nome deste querido pet é {pet['nome'].title()}, o seu dono é {pet['dono'].title()}, ele ou ela tem {pet['idade']} aninhos, e sua raça é {pet['raça'].title()}")