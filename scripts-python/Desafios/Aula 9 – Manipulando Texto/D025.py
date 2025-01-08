# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite seu nome completo: ")
comparativo = "Silva" in nome
print(f"Seu nome completo é {nome}. Vejamos se você tem 'Silva' em alguma parte do nome: {comparativo}")
