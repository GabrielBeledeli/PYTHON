# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('=-='*20)
print('{:^60}'.format('Jogo da Adivinhação'))
print('=-='*20)
num = int(input('Adivinhe um número de 0 a 5: '))
pensar = random.randint(0, 5)
if num == pensar:
    print('Você acertou, parabês!!')
else:
    print('Você errou!!')