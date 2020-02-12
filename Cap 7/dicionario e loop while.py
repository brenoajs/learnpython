responses = {}

polling_active = True

while polling_active:
    name = input("\n Qual seu nome?: ")
    response = input("Qual montanha você gostaria de escalar um dia?: ")
    
    responses[name] = response 

    repeat = input("Você gostaria que outra pessoa respondesse? (yes/no) ")
    if repeat == 'no':
        polling_active = False 

print("\n--- Resultados: ---")
for name, response in responses.items():
    print(f"{name.title()} gostaria de escalar o {response.title()}.")
    