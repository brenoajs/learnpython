def order(*itens):
	print(f"\nVou preparar o sanduíche mais moral da cidade para você!")
	for item in itens:
		print(f"...Adicionando {item} ao seu sanduíche")
	print(F"\nSeu pedido está pronto!")


order('carrapato', 'jiraya')
order('maconha', 'sapato sujo', 'genipapo')
order('giló', 'alfazema', 'medicina')