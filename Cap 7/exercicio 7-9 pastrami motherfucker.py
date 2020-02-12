# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:00:57 2019

@author: brenojaruzo
"""

sanduiche_order = ['pastrami', 'hamburguer','pastrami', 'pastrami', 'cheeseburguer', 'cheesebacon','cheesetudo']
sanduiches_finalizados = []
sanduiches_cancelados = []

print("Olá! boa tarde. Gostariamos de avisar que estamos momentaneamente sem Pastrani e portanto os pedidos serão cancelados.\n")

while 'pastrami' in sanduiche_order:
    removidos = sanduiche_order.remove('pastrami')

while sanduiche_order:
	sanduiche = sanduiche_order.pop()
	print(f"O {sanduiche} está sendo preparado...")
	sanduiches_finalizados.append(sanduiche)
    
print("\n")
print("--- Os sanduíches abaixo foram finalizados: ---")
for sanduichepronto in sanduiches_finalizados:
    print(f"{sanduichepronto}")
    