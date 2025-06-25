import mysql.connector
from conectar import conexion

print("Bienvenido a Crear un nuevo registro")

def crear():
    print("Ingrese los datos del nuevo registro:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    email = input("Email: ")
    conn = conexion()

    try:
        cursor = conn.cursor()
        consulta = "INSERT INTO ususarios (nombre, edad, email) VALUES (%s, %s, %s)"
        datos = (nombre, edad, email)
        cursor.execute(consulta, datos)
        conn.commit()

       

        print(f"Registro creado con éxito:\nNombre: {nombre}\nEdad: {edad}\nEmail: {email}")
        
    except mysql.connector.Error as error:
        print(f"Error al insertar en la base de datos: {error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    print("Volver al menu principal?")
    volver = input()
    if volver.lower() == "si":
        from main import main
        main()
    else:
        print("Cerrando Proceso...")
        exit(0)
