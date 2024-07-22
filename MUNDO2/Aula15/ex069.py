maior = 0
homem = 0
m_menor20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        maior += 1
    if 'M' in sexo:
        homem += 1
    if 'F' in sexo and idade < 20:
        m_menor20 += 1

    condi = ' '
    while condi not in 'SN':
        condi = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if 'N' in condi:
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homem cadastrados')
print(f'E temos {m_menor20} mulheres com menos de 20 anos')
