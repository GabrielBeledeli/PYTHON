#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import pow, sqrt
co = float(input('Cateto oposto '))
ca = float(input('Cateto adjacente '))
h = sqrt(co**2 + ca**2)
print('A hipotenusa é {:.2}'.format(h))
