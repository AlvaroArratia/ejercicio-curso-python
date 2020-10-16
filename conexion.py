import mysql.connector


def conectar():
    database = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database="master_python",
                                       port=3306)
    cursor = database.cursor(
        buffered=True
    )  # El parametro buffered sirve para que el mismo cursor pueda ejecutar varias consultas
    return database, cursor
