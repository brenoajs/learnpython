# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:18:45 2019

@author: brenojaruzo
"""

dream_vacation = {}
polling_active = True


while polling_active:
    name = input("Olá! Qual o seu nome? ")
    local_dos_sonhos = input("Se você pudesse escolher o local dos sonhos, onde seria? ")
    
    dream_vacation[name] = local_dos_sonhos
    pergunta = input("Deseja acrescentar mais pessoas e local dos sonhos? (Y/N): ")
    
    if pergunta == 'n':
        polling_active = False
        print("\n")
        
print("---Essas são as pessoas e seus resultados bacanudos: ---")
for name, local in dream_vacation.items():
    print(f"{name.title()} tem como sonho ir para {local.title()}")