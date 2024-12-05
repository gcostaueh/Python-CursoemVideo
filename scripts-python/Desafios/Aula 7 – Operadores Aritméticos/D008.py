# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite a quantidade de metros: '))
centimetro = metro * 100
milimetro = metro * 1000

print(f'Você digitou {metro} metro(s). Isso equivale a {centimetro} centímetro(s) e {milimetro} milímetro(s).')

#No vídeo de resolução do desafio, o professor passou mais uma parte desse desafio, como um desafio bonus, que era adicionar também as medidas de decímetros, decâmetros, hectómetros e quilómetros. Segue abaixo a resolução:

a = float(input('Digite um valor em metro: '))
print(f'a medida de {a} metros é igual a {a*10} decímetros')
print(f'a medida de {a} metros é igual a {a*100} centímetros')
print(f'a medida de {a} metros é igual a {a*1000} milímetros')
print(f'a medida de {a} metros é igual a {a/10} decâmetros')
print(f'a medida de {a} metros é igual a {a/100} hectómetros')
print(f'a medida de {a} metros é igual a {a/1000} quilómetros')
