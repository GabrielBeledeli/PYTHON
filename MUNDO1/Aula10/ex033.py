# xercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

menor = a
if b<menor and b<c:
    menor = b
if c<menor and c<b:
    menor = c
maior = a
if b>maior and b>c:
    maior = b
if c>maior and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))