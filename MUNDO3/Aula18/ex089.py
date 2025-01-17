# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    cond = ' '
    while cond not in 'NS':
        cond = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
print('='*35)
print(f'{'nº':<4}{'NOME':<10}{'MÉDIA':>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*35)
    opc = int(input('Mostrar nota de qual aluno? (999 Stop) '))
    if opc == 999:
        print('FINALIZADO...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE!')