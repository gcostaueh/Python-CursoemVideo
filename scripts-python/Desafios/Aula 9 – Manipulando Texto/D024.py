# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input("Digite o nome da sua cidade: ")
resultado = "Santo" in cidade
print(f"A cidade digitada foi {cidade}, vejamos se ela possui 'Santo': {resultado}")

# Resolução do Guanabara

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == "SANTO")

