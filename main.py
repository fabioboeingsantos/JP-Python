from modelos import Alunos

def menu_simples():
    print('='*30)
    print(f'\n{"Cadastro de alunos":^30}')
    print('\n(1) - Cadastrar Aluno')   
    print('(2) - listar alunos')
    print('(3) - Buscar aluno por ID')
    print('(0) - Sair')
    print('\n' +'='*30)

def cadastrar():
    sql = "INSERT INTO alunos (nome, nota) VALUES (%s, %s)"
    input("Digite o nome do aluno: ")
    nota = input("Digite a nota do aluno: ")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(sql, (nome, nota))
    conexao.commit()
    conexao.close()


def listar_alunos():
    for produto in listar_alunos():
        produto.exibir()

def buscar_aluno():
    id = int(input("Digite o ID do aluno: "))
    
    

while True:
    menu_simples()
    opcao = input("Digite uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar_alunos()
    
        

    else:
        print("Opção inválida! Tente novamente.")