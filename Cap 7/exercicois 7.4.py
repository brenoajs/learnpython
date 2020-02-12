# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:54:13 2019

@author: brenojaruzo
"""

#7.4 Pizza Toppings!

prompt = "Olá! bem vindo a pizzaria do Breninho!"
prompt += "\nTemos vários tipos de pizza disponíveis"
prompt2 = "\nCaso você queira parar, digite PARAR"
prompt2 += "\nVocê poderia me informar quais os tipos de topping você gostaria para sua pizza? "

print(prompt)

while True:
    print(prompt2)
    mensagem = input()
    
    if mensagem == 'PARE':
        break
    else:
        print(f"Adicionando {mensagem} na pizza...")