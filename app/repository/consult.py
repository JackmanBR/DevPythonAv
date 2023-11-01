import mysql.connector

#CONSULTAR DADOS DO BANCO
def dataConsult():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="pythonav"
        )

        cursor = db.cursor()

        query = "SELECT * FROM `process`"

        cursor.execute(query)

        results = cursor.fetchall()

        for row in results:
            print(row)

    except mysql.connector.Error as err:
        print(f"Erro: {err}")


        cursor.close()
        db.close()
