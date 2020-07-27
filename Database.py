import sqlite3

def createTable():
	connection = sqlite3.connect("login.db")
	connection.execute("CREATE TABLE TEXTO(PARAGRAFO TEXT NOT NULL)")
	#connection.execute("INSERT INTO USERS VALUES(?,?)", ('sasusaku', 'euteamo', 0))
	connection.commit()
	#result = connection.execute("SELECT * FROM USERS")

	connection.close()
"""
def insertFrase(frase):
	connection = sqlite3.connect("login.db")
	cursor = connection.cursor()
	cursor.execute("INSERT INTO FRASES(FRASE) VALUES(?)", (frase))
	connection.commit()
	
	cursor.execute("SELECT * FROM FRASES")
	connection.commit()

	for i in cursor.fetchall():
		print(i)
	
	connection.close()
"""
#createTable()

i = 0
while(i == 0):
	frase = input("frase: ")
	print(frase)

	connection = sqlite3.connect("login.db")
	#cursor = connection.cursor()
	connection.execute("INSERT INTO FRASES(FRASE) VALUES(?)", (frase))
	connection.commit()

	cursor.execute("SELECT * FROM FRASES")
	connection.commit()

	for i in cursor.fetchall():
		print(i)

	connection.close()
	#insertFrase(frase)

