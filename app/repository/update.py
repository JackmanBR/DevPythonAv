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

        id_process = id

        cursor.execute("SELECT * FROM process WHERE id = %s", (id_process,))
        processo = cursor.fetchone()

        if processo is None:
            print("O ID informado não foi encontrado na tabela.")
        else:
            new_process = process
            new_autor = author

            cursor.execute("UPDATE process SET processo = %s, autor = %s WHERE id = %s", (new_process, new_autor, id_process))
            conn.commit()
            print("Valores atualizados com sucesso,retornando ao menu inicial!")

    except mysql.connector.Error as err:
        print("Erro MySQL:", err)

    finally:
        # Feche a conexão com o banco de dados, independentemente de qualquer exceção
        if conn:
            conn.close()





