# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print(f'O número digitado foi: {n1}!\nO dobro desse valor equivale à {dobro}!\nJá o triplo equivale à {triplo}!\nE por fim, a raiz quadrada desse valor equivale à {raiz:.2f}!')