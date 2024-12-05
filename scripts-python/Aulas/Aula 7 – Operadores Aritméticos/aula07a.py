n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaointeira = n1 // n2
exponenciacao = n1 ** n2

print(f'A soma vale {soma}')
print(f'A subtração vale {subtracao}')
print(f'A multiplicação vale {multiplicacao}')
print(f'A divisão vale {divisao:.3f}')
print(f'A divisão inteira vale {divisaointeira}')
print(f'A exponenciação vale {exponenciacao}\n')

#Print Único
print(f'A soma vale {soma};\nA subtração vale {subtracao};\nA multiplicação vale {multiplicacao};\nA divisão vale {divisao};\nA divisão inteira vale {divisaointeira};\nA exponenciação vale {exponenciacao}!', end=" =D ")
print('Obrigado por ter lido até aqui!')