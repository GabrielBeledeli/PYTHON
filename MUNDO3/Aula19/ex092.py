# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
funcionarios = dict()
funcionarios['Nome'] = str(input('Nome: '))
funcionarios['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
funcionarios['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if funcionarios['CTPS'] != 0:
    funcionarios['Contratação'] = int(input('Ano de Contratação: '))
    funcionarios['Sálario'] = float(input('Sálario: '))
    ano_atual = date.today().year
    funcionarios['Idade'] = (ano_atual - funcionarios['Ano de Nascimento'])
    funcionarios['Aposentadoria'] = funcionarios['Idade'] + ((funcionarios['Contratação'] +35 ) - ano_atual)
for k, v in funcionarios.items():
    print(f' - {k:.<30}{v:>}')