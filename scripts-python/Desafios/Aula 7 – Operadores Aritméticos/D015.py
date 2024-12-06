# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60, por dia e R$0,15 por KM rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM rodados? '))

preco_dias = dias *  60
preco_km = km * 0.15
preco_total = preco_dias + preco_km

print(f'O total a pagar é de R${preco_total:.2f}')

