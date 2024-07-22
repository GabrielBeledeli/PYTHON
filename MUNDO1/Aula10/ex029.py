# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Digite a sua velocidade: '))
if v > 80:
    m = 7.0*(v - 80)
    print('Sua multa é de R${:.2f}'.format(m))
print('Tenha m bom dia, dirija com segurança!')