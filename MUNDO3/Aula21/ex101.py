# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano_nsc):
    ano_atual = date.today().year
    idade = ano_atual - ano_nsc
    if idade < 16:
        return f'Com {idade} anos NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos VOTO OPICIONAL!'
    else:
        return f'Com {idade} anos VOTO OBRIGATÓRIO!'
# principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))