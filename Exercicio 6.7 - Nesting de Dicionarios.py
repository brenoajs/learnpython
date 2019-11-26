moradores_da_aurora = {
    'ian': {
        'first_name': 'Ian',
        'last_name': 'Chaves',
        'idade': 28,
        'cidade': 'Recife',
    },
    'breno': {
        'first_name': 'Breno',
        'last_name': 'Jaruzo',
        'idade': 28,
        'cidade': 'Recife',
    },
    'rafael': {
        'first_name': 'Rafael',
        'last_name': 'Mattos',
        'idade': 29,
        'cidade': 'Recife',
    },

}

for pessoas, valores in moradores_da_aurora.items():
    print(f"O nosso amigo{valores['first_name']} {valores['last_name']} que tem {valores['idade']} nasceu na belíssima cidade de {valores['cidade']}")

print(moradores_da_aurora)

#pra acessar os valores que tão dentro do nest do dicionário você tem que criar variáveis que consigam acessar os valores. 
#ex full_name = f"{user_info['first']} e aí usa essa variável para loopar e acessar os valores que estão dentro do dicionário

#    print(f"{valores['first_name']} {valores['last_name']}")
#    print(f"{valores['idade']}")
#    print(f"{valores['cidade']} \n")