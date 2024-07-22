# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metro = float(input('Digite uma valor em metro:'))
km = metro / 1000
hm = metro / 100
dm = metro / 10
dc = metro * 10
cm = metro * 100
mm = metro * 10000
print('A mediade de {} corresponde a \n{}km\n{}hm\n{}dm\n{:.0f}dc\n{:.0f}cm\n{:.0f}mm'.format(metro,km,hm,dm,dc,cm,mm))