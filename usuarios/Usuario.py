import mysql.connector
from datetime import datetime
from conexion import conectar

database, cursor = conectar()


class Usuario:

    nombre: str
    apellido: str
    email: str
    passwd: str

    def __init__(self, nombre, apellido, email, passwd):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.passwd = passwd

    def crear_usuario(self):
        try:
            sql_request = f"INSERT INTO usuarios VALUES (null, '{self.nombre}', '{self.apellido}', '{self.email}', '{self.passwd}', '{datetime.now()}')"
            cursor.execute(sql_request)
            database.commit()
            return True
        except Exception as err:
            print("Error al crear el usuario. " + str(type(err).__name__) +
                  ": " + str(err))

    def buscar_usuario(self):
        try:
            sql_request = f"SELECT * FROM usuarios WHERE email='{self.email}' AND pass='{self.passwd}'"
            cursor.execute(sql_request)
            usuario_info = cursor.fetchone()
            return usuario_info
        except Exception as err:
            print("Error al encontrar el usuario. " + str(type(err).__name__) +
                  ": " + str(err))

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_passwd(self, passwd):
        self.passwd = passwd

    def get_passwd(self):
        return self.passwd
