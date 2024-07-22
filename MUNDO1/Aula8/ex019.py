# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
nome1 = input('Digite o primeiro nome ')
nome2 = input('Digite o sengondo nime ')
nome3 = input('Digite o terceiro nome ')
nome4 = input('Digite o quarto nome ')

sorte = random.choice(nome1, nome2, nome3, nome4)
print('O nome do aluno escolhido é {}'.format(sorte))