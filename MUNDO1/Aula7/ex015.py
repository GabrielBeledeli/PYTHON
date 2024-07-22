#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Insira os km percorridos: '))
dias = int(input('Insira a quantidade de dias: '))
custo_dia = dias*60
custo_km = km*0.15
print('O preço do aluguel será: R${}'.format(custo_dia+custo_km))