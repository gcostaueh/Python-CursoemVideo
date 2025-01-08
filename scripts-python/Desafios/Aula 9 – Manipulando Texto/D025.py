# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite seu nome completo: ")
comparativo = "Silva" in nome
print(f"Seu nome completo é {nome}. Vejamos se você tem 'Silva' em alguma parte do nome: {comparativo}")

#Correção do Guanabara

nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')
