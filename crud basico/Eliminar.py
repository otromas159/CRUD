import mysql.connector
from conectar import conexion

print("Bienvenido a Editar un registro")

def eliminar():

    print("ingrese la id del registro que desea Eliminar")
    id = input("id: ")
    conn = conexion()

    try:
        cursor = conn.cursor()
        consulta = "DELETE FROM ususarios WHERE id = %s"
        datos = (id,)
        cursor.execute(consulta, datos)
        conn.commit()

       

        print("Eliminacion exitosa")
        
    except mysql.connector.Error as error:
        print(f"Error al Eliminar en la base de datos: {error}")
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
