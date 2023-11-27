import mysql.connector

connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pj_db"
        )
cursor = connection.cursor()

cursor.execute('CREATE TABLE CADASTRO(email int, usuário char(20), senha int)')