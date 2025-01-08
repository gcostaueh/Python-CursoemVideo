# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = input("Digite seu nome completo: ")
nomes = nome.split()
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f'O nome digitado foi: {nome}')
print(f"O seu primeiro nome é: {primeiro_nome}")
print(f"O seu último nome é: {ultimo_nome}")
