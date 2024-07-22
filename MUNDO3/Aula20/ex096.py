# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(comprimento, largura):
    print(f'A área de um terreno com {comprimento}x{largura} é de {comprimento*largura} m²')
print(f'{'controle de Terrenos':^40}')
print('='*40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)