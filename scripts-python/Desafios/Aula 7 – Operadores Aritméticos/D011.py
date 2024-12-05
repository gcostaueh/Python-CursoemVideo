# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta_necessaria = area / 2

print(f"A parede tem dimensão de {largura}x{altura} metros, com uma área de {area:.2f}m².")
print(f"Você precisará de {tinta_necessaria:.2f} litro(s) de tinta para pintá-la.")

