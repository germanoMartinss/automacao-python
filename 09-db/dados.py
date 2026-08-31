import sqlite3

#1 - Conectando no banco de dados
def conecta_db():
    conexao = sqlite3.connect("titulo.db")
    return conexao

#2 - Inserindo dados
def insere_dados(titulo, ano, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO filmes (titulo, ano, nota)
        VALUES (?, ?, ?)
    """, (titulo, ano, nota))
    conexao.commit()
    conexao.close()

#3 - Listando dados
def lista_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    conexao.close()
    return dados