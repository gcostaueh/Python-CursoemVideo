# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário do funcionário: R$"))
aumento = salario * 0.15
novosalario = salario + aumento

print(f"O salário que era R$ {salario:.2f}, com 15% de aumento, passou a receber R$ {novosalario:.2f}.")
