# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Insira seu ano de nascimento: '))
atual = date.today().year
print('Voce nasceu em {} tem {} anos em {}'.format(ano, (-ano+atual), '2024'))
if -ano+atual > 18:
    print('Já deveria ter se Alistado a {} anos\nSeu alistamento sera em {}'.format((-ano+atual)-18, ((-ano+atual)-18)+atual))
elif -ano+atual == 18:
    print('Alistesse Imediatamente')
elif -ano+atual < 18:
    print('Você esta com o alistamento pendente a {} anos'.format((ano-atual)+18))
else: print('Erro, tente Novamente!!')