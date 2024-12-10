# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
nomes = ['Maria', 'João', 'Ana', 'Carlos']
escolhido = random.choice(nomes)

print(f'O aluno escolhido para apagar o quadro foi: {escolhido}')
