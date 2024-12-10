# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
nomes = ['Maria', 'João', 'Ana', 'Carlos']
escolhido = random.choice(nomes)

print(f'O aluno escolhido para apagar o quadro foi: {escolhido}')

# Solução do GUANABARA:

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
escolha = random.choice(alunos)
print(f'O aluno escolhido foi {escolha}')
