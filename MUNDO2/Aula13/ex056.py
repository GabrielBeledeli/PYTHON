# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = 0
cont_mulher_20 = 0
for c in range(1, 5):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: [M/F] ')).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        nome_mais_velho = nome
        maior_idade_homem = idade
    if sexo in 'Mm' and idade > maior_idade_homem:
        nome_mais_velho = nome
        maior_idade_homem = idade
    if sexo in 'Ff' and idade < 20:
        cont_mulher_20 += 1
media_idade = soma_idade/4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont_mulher_20))