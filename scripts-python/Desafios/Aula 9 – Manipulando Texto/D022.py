# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
primeiro_nome = nome.split()[0]

print(f'Seu nome com todas as letras MAIÚSCULAS: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')
print(f'Seu nome possui {len(nome.replace(' ', ''))} letras')
print(f'Seu primeiro nome é {primeiro_nome} e a quantidade de letras é {len(primeiro_nome)}')