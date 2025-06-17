import mysql.connector

def conexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crud"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
