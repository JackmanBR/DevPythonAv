import mysql.connector
from mysql.connector import errorcode
#CRIAR CONEXÃO BANCO DE DADOS
def dbConnection():
	try:
		conn = mysql.connector.connect(host='localhost',
												user='root',
												password='123456',
												database='pythonav')
		print("Conectado no banco com sucesso!")
	except mysql.connector.Error as error:
		if error.errno == errorcode.ER_BAD_DB_ERROR:
			print("A base de dados não existe!")
		elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Usuário ou senha inválidos!")
		else:
			print(error)
	else:
		conn.close()

