# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = input('Digite um número entre 0 e 9999: ')
print('Segue abaixo a ordem dos números: ')
print(f'Milhar: {numero[0]}')
print(f'Centena: {numero[1]}')
print(f'Dezena: {numero[2]}')
print(f'Unidade: {numero[3]}')
