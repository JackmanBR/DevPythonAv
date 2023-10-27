import mysql.connector

def dataDelete(id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="pythonav"
    )

    id = 1

    cursor = db.cursor()

    sql = "DELETE FROM process WHERE id = %s"

    try:
        cursor.execute(sql, (id,))
        db.commit()
        print(f"Registro com ID {id} apagado com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        db.close()
