# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").strip()
quantidade_a = frase.lower().count("a")
primeira_posicao = frase.lower().find("a") + 1
ultima_posicao = frase.lower().rfind("a") + 1

print(f"A letra 'A' aparece {quantidade_a} vezes na frase digitada.")
print(f"A primeira ocorrência da letra 'A' está na posição {primeira_posicao}")
print(f"A última ocorrencia da letra 'A' está na posição {ultima_posicao}")
