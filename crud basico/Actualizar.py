import mysql.connector
from conectar import conexion

print("Bienvenido a Editar un registro")

def editar():

    print("ingrese la id del registro que quiere editar")
    id = input("id: ")

    print("Ingrese los datos corregidos:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    email = input("Email: ")
    conn = conexion()

    try:
        cursor = conn.cursor()
        consulta = "UPDATE ususarios SET nombre = %s, edad = %s, email = %s WHERE id = %s"
        datos = (nombre, edad, email, id)
        cursor.execute(consulta, datos)
        conn.commit()

       

        print(f"Registro Editado con éxito:\nNombre: {nombre}\nEdad: {edad}\nEmail: {email}")
        
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
