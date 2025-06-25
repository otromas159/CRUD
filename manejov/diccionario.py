diccionario = {
    "nombre": "Camilo",
    "edad": "19",
}

claves = diccionario.keys()
valores = diccionario.values()
diccionario["apellido"] = "Gonzalez"
del diccionario["edad"]

print("Diccionario:", diccionario)
print("Claves:", claves)
print("Valores:", valores)
print("Longitud del diccionario:", len(diccionario))
