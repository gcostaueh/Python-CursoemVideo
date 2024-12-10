# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = ['Maria', 'João', 'Ana', 'Carlos']
shuffle(alunos)

print(f'A ordem de apresentação dos trabalhos será: {alunos}')

# Solução do GUANABARA:

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
escolha = [n1, n2, n3, n4]
shuffle(escolha)

print(f'A ordem de apresentação dos trabalhos será: {escolha}')
