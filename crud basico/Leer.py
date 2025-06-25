import mysql.connector
from conectar import conexion

print("Bienvenido a Leer registros de la base de datos")

def leer():
    print("\nRegistros de la base de datos:")

    conn = conexion()


    try:
        cursor = conn.cursor()
        consulta = "SELECT * FROM ususarios"
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        if resultados:
            for fila in resultados:
                id, nombre, edad, email = fila
                print(f"Id: {id} | Nombre: {nombre} | Edad: {edad} | Email: {email}")
        else:
            print("No hay registros en la base de datos.")

    except mysql.connector.Error as error:
        print(f"\nError al leer de la base de datos: {error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    print("\n¿Volver al menú principal? (si/no):")
    volver = input()
    if volver.lower() == "si":
        from main import main
        main()
    else:
        print("Cerrando proceso...")
        exit(0)
