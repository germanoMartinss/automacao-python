import sqlite3

#1 - Conectando no banco de dados
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#2 - Excluir dados
cursor.execute("""
    DELETE FROM filmes
    WHERE titulo = 'Devoradores de Estrelas'
""")

#3 - Fechando a conexão
conexao.commit()
conexao.close()
print("Dados excluidos com sucesso!")