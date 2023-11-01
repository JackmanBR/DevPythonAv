import mysql.connector

#CRIAR TABELA NO BANCO

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="pythonav"
)

cursor = conexao.cursor()

comando_sql = """
CREATE TABLE process (
    id INT AUTO_INCREMENT PRIMARY KEY,
    processo VARCHAR(255),
    autor VARCHAR(255)
)
"""

cursor.execute(comando_sql)

conexao.commit()
conexao.close()

print("Tabela criada com sucesso!")