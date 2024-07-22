# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Aquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)

cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoa', 'Sair do sistema'])
    if resposta == 1: # listar conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2: # cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! digite uma opção Válida.\033[m')
    sleep(1)