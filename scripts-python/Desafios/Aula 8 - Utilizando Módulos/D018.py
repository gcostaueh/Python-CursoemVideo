# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

graus = int(input('Digite o valor (em graus) para calcularmos o Seno, Cosseno e Tangente: '))

converte_radianos = math.radians(graus)

print(f'Foi digitados {graus}º. Segue os Valores:')
print(f'Seno: {math.sin(converte_radianos):.3f}')
print(f'Cosseno: {math.cos(converte_radianos):.3f}')
print(f'Tangente: {math.tan(converte_radianos):.3f}')

