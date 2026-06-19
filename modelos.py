from sqlite3 import Cursor
from conexao import conectar
import conexao


class Produto:
    def __init__(self, nome, preco, categoria, ativo=True, id=None, criado_em=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.ativo = ativo        
        self.criado_em = criado_em

    def exibir(self):
        texto = f'''
        codigo:     {self.id}
        nome:       {self.nome}
        preco:      {self.preco}
        categoria:  {self.categoria}
        ativo:      {self.ativo}
        criado em:  {self.criado_em}
        '''
        print(texto)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO produto (nome, preco, categoria, ativo) VALUES (%s, %s, %s, %s)" 
        cursor.execute(sql, (self.nome, self.preco, self.categoria, self.ativo))
       
        '''usar o %s --> Ele avisa ao banco de dados onde colocar cada valor,
        garantindo proteção total contra invasões (SQL Injection) e formatação automática de textos, números e datas.'''

        conexao.commit()
        cursor.close()
        conexao.close()

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM produto"
    cursor.execute(sql)

    produtos = []

    for id, nome, preco, categoria, ativo, criado_m in cursor.fetchall():

        produto = Produto(
            nome=nome, 
            preco=preco, 
            categoria=categoria, 
            ativo=ativo, 
            id=id, 
            criado_em=criado_m
        )

        produtos.append(produto)
    
    cursor.close()
    conexao.close()
    return produtos


