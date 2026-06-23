from conexao import conectar

class Alunos:
    def __init__(self, nome, e_mail, id_alunos, media):
        self.id = id
        self.nome = nome
        self.e_mail = e_mail
        self.id_alunos = id_alunos
        self.media = media
       
    def exibir(self):
        texto = f"""
        Código: {self.id}
        Nome: {self.nome}
        Preco: {self.e_mail}
        Categoria: {self.id_alunos}
        Ativo: {self.media}
        """
        print(texto)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
        
        sql = "INSERT INTO produto (nome, media) VALUES (%s, %s)"
        cursor.execute(sql, (self.nome, self.media))

        conexao.commit()
        conexao.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM produto"
    cursor.execute(sql)
    
    Alunos = []
    for id, nome, nota in cursor.fetchall():
        Alunos = Alunos(id, nome, nota)

    conexao.close()
    return Alunos





