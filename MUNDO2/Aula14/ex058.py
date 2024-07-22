# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = int(randint(0,10))
print('Olá sou o seu computador\nPensei em um número...\nDuvido você adivinhar!')
acertou = False
cont = 0
while not acertou:
    usuario = int(input('Qual o seu palpite? '))
    if usuario == computador:
        acertou = True
        cont += 1
    if usuario > computador:
        print('Menos... Tente mais uma vez.')
        cont += 1 
    if usuario < computador:
        print('Mais... Tente mais uma vez.')
        cont += 1
print('Parabéns você acertou na {}º tentativa!!'.format(cont))
