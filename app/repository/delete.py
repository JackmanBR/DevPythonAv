import mysql.connector

#DELETAR DADO DO BANCO
def deleteDataProcess(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="pythonav"
    )

    cursor = conn.cursor()

    try:

        idToDelete = id

        delete_query = "DELETE FROM process WHERE id = %s"
        cursor.execute(delete_query, (idToDelete,))

        conn.commit()

        print(f"Registros com ID {idToDelete} foram excluídos com sucesso.")

    except mysql.connector.Error as error:
        print(f"Erro ao excluir registros: {error}")

    finally:
        cursor.close()
        conn.close()
