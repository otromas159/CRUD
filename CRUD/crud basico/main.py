def main():
    print("Bienvenido al CRUD desde 0, escoja la opcion que quiera realizar")
    print("1. Crear un nuevo registro")
    print("2. Leer un registro")
    print("3. Actualizar un registro")
    print("4. Eliminar un registro")
    print("5. Salir del programa")

    dato = input("escoja la opcion que desea realizar: ")

    if dato == "1":
        from Crear import crear
        crear()
    elif dato == "2":
        from Leer import leer
        leer()
    elif dato == "3":
        from Actualizar import editar
        editar()
    elif dato == "4":
        from Eliminar import eliminar
        eliminar()
    elif dato == "5":
        exit(0)
    else:   
        exit(0)
if __name__ == "__main__":
    main()