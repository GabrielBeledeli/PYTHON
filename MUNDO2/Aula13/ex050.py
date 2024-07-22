soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite o {}º numero: '.format(i+1)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))