import psycopg2 
from psycopg2 import Error 
from psycopg2.extras import RealDictCursor
from Controller.config import Db_config

class Database_connection:
    def __init__(self):
         self.config = Db_config

    def get_connection(self):
        try:
            conexion = psycopg2.connect(**self.config)
            if conexion.closed == 0:
                return conexion
        except Error as e:
            print(f"Error al conectar con postgres: {e}")
            return None

    def ejecutar_consulta(self, query, params=None):
            conexion = self.get_connection()
            if not conexion:
                return None
            
            cursor = conexion.cursor(cursor_factory=RealDictCursor)
            try:
                cursor.execute(query, params)
                resultados = cursor.fetchall()
                return resultados
            except Error as e:
                print(f"Error en la consulta SQL: {e}")
                return None
            finally:
                cursor.close()
                conexion.close()