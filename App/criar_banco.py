import mysql.connector

connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
cursor = connection.cursor()

cursor.execute("CREATE DATABASE teste_db")
cursor.execute("USE teste_db")
cursor.execute("CREATE TABLE CADASTRO(email int, usuário char(20), senha int)")