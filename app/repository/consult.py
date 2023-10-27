import mysql.connector


def dataConsult():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="pythonav"
    )

    cursor = db.cursor()

    query = "SELECT * FROM process"

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
