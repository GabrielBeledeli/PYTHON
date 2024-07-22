def aumentar(v = 0):
    v = v + (v*0.1)
    return v
def diminuir(v = 0):
    v = v - (v*0.1)
    return v
def dobro(v = 0):
    v = v*2
    return v
def metade(v = 0):
    v = v/2
    return v
def moeda(v = 0, moeda = 'R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')