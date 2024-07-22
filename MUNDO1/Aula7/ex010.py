# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
money = float(input('Quntos reais voce tem? R$'))
dolar = money / 3.27
print('Voce tera {:.3} dolar'.format(dolar))
