def is_prime(number):
	for i in range(2, int(number)-1):
		if number % i == 0:
			return False
	else:
		return True

teste = is_prime(10)
print(teste)