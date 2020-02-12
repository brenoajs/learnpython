#Exemplos do capítulo 7

name = input("Please enter your name: ")
print(f"Olá {name.title()}, tenha um ótimo dia!")

#Dessa forma abaixo você consegue mostrar vários prompts e criar um input() bem mais limpo:

prompt = "Se você me disser o seu nome, eu consigo personalizar as mensagens que você vê."
prompt += "\nQual o seu primeiro nome? "

name = input(prompt)
print(f"\nOlá, {name.title()}")

#programinha para descobrir se a altura é suficiente para rodar numa montanha russa. A malicia aqui é que você transforma o resultado
#do input em número usando a função int(), caso contrário o pitão não consegue fazer conta. Sempre que você usa o input() ele vai interpr
#tar o resultado como sendo uma string

altura = input("Qual a sua altura, em cm? ")
altura = int(altura)

if altura >= 100:
    print(f"Você tem altura suficiente para ir na montanha russa")
else:
    print("Tu é anão, porra!")

#o modulo operador é bem bacana para esse tipo de coisa, porque ele consegue dizer qual o resto das divisões.
# ex 5%3 = 2, 6%3 = 0

number = input("Escreva um número e eu vou te dizer se ele é par ou impar: ")
number = int(number)

if number % 3 == 1:
    print("O número é impar")
else:
    print("O número é impar")

#introduzindo os loops com while
# o loop for pega uma coleção de itens e executa o bloco daquele código uma vez para cada item da coleção.
#em contraste, o loop while só roda enquanto uma certa condição é verdadeira. 

#EX:

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#essa malicia de += 1 significa current_number = current_number + 1, é um tipo de atalho SAFADINHO do python. 


prompt = "Me diga alguma coisa e eu sempre irei repetir para você"
prompt +=  "\nA não ser que você queira parar, nesse caso, digite parar: "
mensagem = ""

while mensagem != 'parar':
    mensagem = input(prompt)
    print(mensagem)

#a malicia aí acima é que payton precisa de algum valor inicial em mensagem, mesmo que em branco para poder verificar antes de iniciar o loop

#utilizando Break para acabar com um loop while


prompt = "\n Por favor, indique o nome da cidade que você já visitou"
prompt += "\n(Digite 'parar' quando você não quiser mais jogar)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to the {city.title()}")


#utilizando continue para continuar com o loop

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)



usuarios_nao_confirmados = ['alice', 'brian', 'candance']
usuarios_confirmados = []

while usuarios_nao_confirmados:
	usuario_atual = usuarios_nao_confirmados.pop()

	print(f"Verificando o usuario: {usuario_atual.title()}")
	usuarios_confirmados.append(usuario_atual)
    
print("\nOs usuários a seguir foram confirmados:")
for usuario in usuarios_confirmados:
	print(usuario.title())