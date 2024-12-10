# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Eu estava fazendo dessa forma, pois não consegui encontrar forma utilizando o Módulo Math, mas depois joguei no GPT
# e ele me passou um método mais fácil usando o math.hypot.

#hipotenusa = pow(cateto_adjacente, 2) + pow(cateto_oposto, 2)
#raiz_hipotenusa = hipotenusa ** (1/2)

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa do triângulo é {hipotenusa:.2f}")
