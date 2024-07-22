# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l*a
print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(l,a, area))
print('Para pintar a parede serão necessários {}l de tinta'.format(area/2))
