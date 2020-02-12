# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:40:57 2019

@author: brenojaruzo
"""

prompt = "Olá! nos somos do cinema XYZ. Antes de começar, gostariamos de saber sua idade: "
prompt += "Caso deseje encerrar o progama, digite parar"
print(prompt)

while True:
    
    age = input("Por favor, informe sua idade: ")
    print(f"\nOlá, a idade escolhida foi de {age}")
    
    if age == 'parar':
        break
    if age == '':
      age = input("Por favor, digite um número válido: ")
    
    age = int(age)
    if age > 12:
        print(f"Para esta idade de {age}, o preço do ingresso é de R$15,00")
    elif age < 3:
        print(f"Para esta idade de {age}, o preço do ingresso é GRATUÍTO!")
    elif age >= 3:
        print(f"Para esta idade de {age}, o preço do ingresso é R$10,00")
        

        

    
 

