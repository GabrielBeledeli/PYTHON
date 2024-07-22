# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('{:=^36}'.format(' Gerrador de PA '))
p_t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
pa = p_t
condicao = 10
bora = True
contador = 0
while bora:
    cont = 0
    while cont < condicao:
        print('{}'.format(pa), end=' -> ')
        pa += r
        cont += 1
        contador += 1
    print('Pause')
    
    condicao = int(input('Quantos termos voce quer mostrar a mais? '))
    
    if condicao == 0:
        bora = False
print('FIM\nProgressão finalizada com {} termos mostrados.'.format(contador))
