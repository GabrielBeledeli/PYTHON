# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:– EQUILÁTERO: todos os lados iguais– ISÓSCELES: dois lados iguais, um diferente– ESCALENO: todos os lados diferentes
print('\033[32m=-='*20)
print('{:.^60}'.format('Analizador de Triangulos'))
print('=-='*20)
s1 = float(input('\033[mPrimeiro Segmento: '))
s2 = float(input('Segundo Segmento '))
s3 = float(input('Terceiro Segmento '))
if s1 < s2+s3 and s2 <s1+s3 and s3<s1+s2:
    if s1 == s2 == s3:
        print('Os segmentos acima podem formar um triângulo EQUIULÁTERO')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Os segmentos acima podem fromar um triângulo ISÓCELES') 
    elif s1 != s2 or s1 != s3 or s2 != s3:
        print('Os segmentos acima podem formar um triângulo ESCALENO') 
else:
    print('Os segmentos acima não podem formar triangulos')