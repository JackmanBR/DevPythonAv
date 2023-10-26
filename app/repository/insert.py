import mysql.connector

def dataInsert(process, client):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="pythonav"
    )
    mycursor = db.cursor()

    insertQuery = "INSERT INTO process (processo, autor) VALUES (%s, %s);"

    values = (process, client)

    mycursor.execute(insertQuery, values)

    print("No of Record Inserted :", mycursor.rowcount)
    print("Inserted Id :", mycursor.lastrowid)
    db.commit()
    db.close()
