import sqlite3

# Ligacao a base de dados (SQLite)
# con = sqlite3.connect(":memory:")
con = sqlite3.connect("base_dados.db")

cursor = con.cursor()

# Criar a tabela
cursor.execute("CREATE TABLE utilizadores (id INTEGER PRIMARY KEY, nome TEXT)")

# Inserir dados
nome_utilizador = "João'; DROP TABLE utilizadores;--" # Entrada maliciosa
query = "INSERT INTO utilizadores (nome) VALUES (?)"
cursor.execute(query, (nome_utilizador,)) # Parametrização evita a injeção
con.commit()

# Verificando os dados
cursor.execute("SELECT * FROM utilizadores")
print(cursor.fetchall())
