import psycopg2 
from psycopg2 import Error 
from psycopg2.extras import RealDictCursor

class Conexion:

    def __init__(self):
        self.host = "localhost"
        self.usuario = "postgres"
        self.password = "110807"
        self.base_datos = "postgres"

    def conectar(self):
        try:
            conexion = psycopg2.connect(
                host=self.host,
                user=self.usuario,
                password=self.password,
                database=self.base_datos
            )
            return conexion

        except psycopg2.Error as error:
            print("Error al conectar con MySQL:", error)
            return None