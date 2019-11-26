#Exercicio 6.9

favorite_numbers = {
    'ian': [28],
    'breno': [12, 23],
    'rafael': [13],
    'carol': [25, 12],
    'tiago': [13],
}

for pessoas, numeros in favorite_numbers.items():
    print(f"Os números preferidos de {pessoas.title()}:")
    for numero in numeros:
        print(numero)




