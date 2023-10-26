import mysql.connector

def dataUpdate():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="pythonav"
    )
    mycursor = db.cursor()

    oldVar = "1818181818"
    newVar = "99999999"

    try:

        sql = "UPDATE process SET processo = %s WHERE processo = %s"
        mycursor.execute(sql, (newVar, oldVar))

        db.commit()

        print(f"Valor {oldVar} atualizado para {newVar} com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao atualizar valor: {err}")

    finally:

        db.close()
        db.close()


dataUpdate()



