import mysql.connector

def dataUpdate(choice, oldVar, newVar):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="pythonav"
    )
    mycursor = db.cursor()

    try:

        if choice == 1:
            sql = "UPDATE process SET processo = %s WHERE processo = %s"
        if choice ==2:
            sql = "UPDATE process SET autor = %s WHERE autor = %s"
        mycursor.execute(sql, (newVar, oldVar))

        db.commit()

        print(f"Valor {oldVar} atualizado para {newVar} com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao atualizar valor: {err}")

    finally:

        db.close()
        db.close()

dataUpdate()



