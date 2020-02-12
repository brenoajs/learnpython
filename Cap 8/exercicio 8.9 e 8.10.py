lista_de_mensagens = ['Feliz Natal', 'Feliz Ano Novo', 'Feliz Aniversário']
mensagens_enviadas = []


def show_messages(lista_de_mensagens):
	"""Essa função mostra as mensagens contidas numa lista definida acima""" 
	while lista_de_mensagens: 
		print(f"Restam {len(lista_de_mensagens)} mensagens a serem enviadas...")
		mensagem1 = lista_de_mensagens.pop()
		print(f"Enviando a mensagem: \"{mensagem1}\"")
		mensagens_enviadas.append(mensagem1)

	print("\n")
	for mensagem in mensagens_enviadas:
		print(f"A mensagem a seguir foram enviadas com sucesso: \"{mensagem}\"")

	print(f"O total de mensagens a serem enviadas: {len(lista_de_mensagens)}")

show_messages(lista_de_mensagens[:])
#aqui ele vai mandar uma cópia da lista, evitando que você altere a lista original =)

print(lista_de_mensagens)
print(mensagens_enviadas)