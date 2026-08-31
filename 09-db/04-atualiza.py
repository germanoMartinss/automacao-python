import sqlite3

#1 - Conectando no banco de dados
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#2 - Atualizando dados
cursor.execute("""
    UPDATE filmes
    SET nota = 8.5
    WHERE titulo = 'Devoradores de Estrelas'
""")

#3 - Fechando a conexão
conexao.commit()
conexao.close()
print("Dados atualizados com sucesso!")