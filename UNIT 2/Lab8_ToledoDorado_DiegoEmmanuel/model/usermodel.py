import psycopg2
from controller.conexion import Conexion

class UserModel:

    def __init__(self):
        self.conexion_db = Conexion()

    def registrar_usuario(self, nombre, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return "error"

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                INSERT INTO login_mvc.users (name_user, email_user, password_user)
                VALUES (%s, %s, %s)
            """

            cursor.execute(consulta, (nombre, email, password))
            conexion.commit()

            return "ok"

        except psycopg2.errors.UniqueViolation:
            conexion.rollback()
            return "duplicado"

        except psycopg2.Error as error:
            conexion.rollback()
            print("Error al registrar usuario:", error)
            return "error"

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def validar_usuario(self, email, password):
        conexion = self.conexion_db.conectar()

        if conexion is None:
            return None

        cursor = None

        try:
            cursor = conexion.cursor()

            consulta = """
                SELECT id_user, name_user
                FROM login_mvc.users
                WHERE email_user = %s AND password_user = %s
            """

            cursor.execute(consulta, (email, password))
            usuario = cursor.fetchone()

            return usuario

        except psycopg2.Error as error:
            print("Error al validar usuario:", error)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            conexion.close()

    def cerrar(self):
        pass