import mysql.connector

def dataUpdate(id, process, author):
    try:
        # Conecte-se ao banco de dados MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="pythonav"
        )

        cursor = conn.cursor()

        id_processo = id

        cursor.execute("SELECT * FROM process WHERE id = %s", (id_processo,))
        processo = cursor.fetchone()

        if processo is None:
            print("O ID fornecido não foi encontrado na tabela.")
        else:
            novo_processo = process
            novo_autor = author

            cursor.execute("UPDATE process SET processo = %s, autor = %s WHERE id = %s", (novo_processo, novo_autor, id_processo))
            conn.commit()
            print("Valores atualizados com sucesso!")

    except mysql.connector.Error as err:
        print("Erro MySQL:", err)

    finally:
        # Feche a conexão com o banco de dados, independentemente de qualquer exceção
        if conn:
            conn.close()





