# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:48:48 2020

@author: brenojaruzo
"""

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, com formatacao"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


#sobre o teste do if: "if middle_name" pitão automaticamente faz o teste assumindo que essa é uma condição verdadeira
#por isso que não tem nada depois para validar a hipótese, é uma parada automatica
#essa parte do código só vai rodar se tiver esse argumento na função
#caso contrário ele vai pular e rodar o código sem ele :)

def build_person(first_name, last_name, age=None):
    """retornar um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

#usando função com while loop

def get_formatted_name(first_name, last_name):
    """retorna um nome formatado""" 
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print('\nPlease tell me your name: ')
    print("(Enter 'q' at any time to quit)")
    
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")



