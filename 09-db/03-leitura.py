import sqlite3

#1 - Conectando no banco de dados
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()

#2 - Lendo dados
cursor.execute("SELECT * FROM filmes")
for filme in cursor.fetchall():
    print(f"Título: {filme[1]}, Ano: {filme[2]}, Nota: {filme[3]}")