# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ['Maria', 'João', 'Ana', 'Carlos']
random.shuffle(alunos)

print(f'A ordem de apresentação dos trabalhos será: {alunos}')
