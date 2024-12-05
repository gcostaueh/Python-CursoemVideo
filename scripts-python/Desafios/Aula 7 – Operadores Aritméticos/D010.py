# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere o valor US$1,00 = R$3,27.

carteira = float(input('Digite quantos "R$" você tem disponível para comprar "US$": '))
dolar = 3.27
conversao = carteira / dolar

print(f'Você informou que possui R${carteira} destinados a comprar US$. Fazendo a conversão com o valor do dólar à R${dolar}, é possível comprar US${conversao:.2f}!')
