from math import prod
from modelos import Produto, listar_produtos


def menu_simples():
    print('='*30)
    print(f'\n{"Menu de produtos ":^30}')
    print('\n(1) - Cadastrar produto')     
    print('(2) - listar alunos')
    print('(0) - Sair')
    print('\n' +'='*30)



def cadastrar():
    nome = input('Digite seu nome: ')
    preco = float('Digite o preco: ')
    categoria = input('Digite a categoria: ')

    produto = Produto(nome, preco, categoria)
    produto.salvar()

def listar():
    for produto in listar_produtos():
        produto.exibir()
while True:
    menu_simples()
    Opcao = input('Digite sua opcao: ')

    if Opcao == '0':
        break

    elif Opcao == '1':
      cadastrar()
    
    elif Opcao == '2':
        listar()      

    
    else:
        print('Opcao invalida')