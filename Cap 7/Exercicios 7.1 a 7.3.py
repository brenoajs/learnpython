#Exercicio 7.1, 7.2 e 7.3 do Capítulo 7
#Feito por Breno Jaruzo
#26.11.2019

#7.1
carro = input("Que tipo de carro você gostaria de alugar?: ")
print(f"Ok! deixe-me ver se consigo encontrar um(a) {carro.title()} para você.")

#7.2

lugares = input("Olá! quantos lugares na mesa você precisa para a sua reserva?: ")
lugares = int(lugares)

if lugares > 8:
	print("Infelizmente para esta quantidade de pessoas não temos disponibilidade imediata. Aguarde um pouco")
else:
	print("Olá! temos disponibilidade imediata, nos acompanhe por favor.")

#7.3 

#a malicia aqui é que você coloca uma variavel atrelada ao texto que você quer que apareça e só no final você pede pelo Input do usuário.

numero = "Olá! este programinha informa se o seu número é um multiplo de 10 ou não"
numero += "\nVocê poderia nos informar o número, por favor?: "

numero = input(numero)
numero = int(numero)

if numero % 10 == 0:
	print("Parabéns! o número escolhido pode ser dividido por 10.")
else:
	print("Epa! esse teu número é safadinho, ein? tente novamente.")