# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input('Digite o {} ano: '.format(c+1)))
    if (-ano+2024) >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas atingiram a maioridade\n{} pessoas não atingiram a maioridade'.format(maior,menor))