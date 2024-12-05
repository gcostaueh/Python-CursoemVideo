# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Digite o nome do Aluno que você quer calcular a média: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média final do aluno(a) {nome} foi: {media:.1f}!')
