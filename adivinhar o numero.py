import random

numero_a_ser_adivinhado = random.randint(0,20)
numero_digitado = []

print("Olá! Vamos brincar de adivinhação.")

while True:
	print("Caso você queira sair, apenas digite 100")
	print("Escolha um número de 1 a 20: ")
	numero_digitado = int(input())


	if numero_digitado == numero_a_ser_adivinhado:
		print("\nParabéns! Você venceu o jogo!")
		print(f"O número escolhido foi {numero_a_ser_adivinhado}")
		print("---Obrigado por ter jogado---")

		break
	elif numero_digitado == 100:
		print("---Obrigado por ter jogado---")
		break
	else:
		print("\nVocê não acertou dessa vez, vamos tentar novamente? ")