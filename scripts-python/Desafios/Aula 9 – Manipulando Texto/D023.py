# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um número entre 0 e 9999: '))
n = str(numero)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Segue abaixo a ordem dos números: ')
print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')
