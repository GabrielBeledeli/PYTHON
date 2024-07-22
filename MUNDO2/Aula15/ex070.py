'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
print('-'*40)

print(f'{'LOJA DO ZÉ':^40}')
print('-'*40)
total = 0
acima_mil = 0
cont_produtos = 0
menor_p = 0
nome_menor_p = ' '
while True:
    cont_produtos += 1
    nome_p = str(input('Nome do Produto: '))
    preco_p = float(input('Preço: R$'))
    total += preco_p

    if preco_p > 1000.00:
        acima_mil += 1

    if cont_produtos == 1:
        menor_p = preco_p
        nome_menor_p = nome_p
    elif preco_p < menor_p:
        menor_p = preco_p
        nome_menor_p = nome_p

    c = ' '
    while c not in 'NS':
        c = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'{' FIM DO PROGRAMA ':=^40}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {acima_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_menor_p} que custa R${menor_p:.2f}')
