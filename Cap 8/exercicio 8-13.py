def build_profile(first, last, **user_info):
	"""Cria um dicionário contendo tudo sobre o usuário"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info


user_profile = build_profile('Breno','Jaruzo',location='Recife',field='Administration',idade=28)

print(user_profile)