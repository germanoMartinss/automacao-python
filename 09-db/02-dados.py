import sqlite3

#1 - Conectando no banco de dados
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#2 - Inserindo dados
cursor.execute("""
    INSERT INTO filmes (titulo, ano, nota)
    VALUES ('Devoradores de Estrelas', 2026, 7.7)
""")

#3 - Fechando a conexão
conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")