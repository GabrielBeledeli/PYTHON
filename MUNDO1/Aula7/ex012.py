# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
desconto = preco - (preco* 5 /100)
print('O produto que custava R%{} agora vai custar R${:.3}'.format(preco,desconto))