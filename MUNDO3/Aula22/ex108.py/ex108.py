# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moedas
valor = float(input('Digite o preço: R$'))
print(f'Aumentando 10%, temos R${moedas.moeda(moedas.aumentar(valor))}')
print(f'Descontando 10%, temos R${moedas.moeda(moedas.diminuir(valor))}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.moeda(moedas.dobro(valor))}')
print(f'A metade de {moedas.moeda(valor)} é {moedas.moeda(moedas.metade(valor))}')