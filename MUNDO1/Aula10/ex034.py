# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o seu salário? R$'))
new_salario = float()
if salario > 1250:
    new_salario = salario + (salario*10/100)
else:
    new_salario = salario + (salario*15/100)
print('Seu salario final será: R${}'.format(new_salario))