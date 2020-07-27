import sqlite3

def createTable():
	connection = sqlite3.connect("login.db")
	#connection.execute("CREATE TABLE USUARIO(LOGIN TEXT NOT NULL,SENHA TEXT,ENTRADA INTEGER)")
	connection.execute("INSERT INTO USERS VALUES(?,?,?)", ('sasusaku', 'euteamo', 0))
	connection.commit()
	result = connection.execute("SELECT * FROM USERS")

	for i in result:
		print("User:", i[0])
		print("Senha:", i[1])
		print("Vezes entradas:", i[2])

	connection.close()

createTable()