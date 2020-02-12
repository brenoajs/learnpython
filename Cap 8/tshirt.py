def make_tshirt(text,size='g'):
	"""Define o tamanho da camiseta e printa uma mensagem bonitinha"""
	print(f"O tamanho da camiseta escolhido foi {size}")
	print(f"A mensagem que será impressa na camiseta será: \"{text}\"")
	print("\n--- Sumário do Pedido --- ")
	print(f"Camiseta \"{size}\" com frase \"{text.title()}\"")
	
make_tshirt(text='i love python')
make_tshirt(text='i love python', 'm')