# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nome = str(input("Em que cidade você nasceu? ")).strip()
print(nome[:5].upper() == 'SANTO')
