# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario + (salario * 15/100)
print('O funcionário ira ganhar R${:.2f}'.format(aumento))