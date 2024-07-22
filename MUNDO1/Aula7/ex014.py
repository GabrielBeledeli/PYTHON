# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a tempratura em °C : '))
f = (celsius * 9/5) + 32
print('{} °C em °F é {}'.format(celsius,f))