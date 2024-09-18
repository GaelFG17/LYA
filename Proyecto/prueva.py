import conector

mydb = conector.conectar_db()

if mydb:
    # Crear un objeto cursor para ejecutar consultas
    mycursor = mydb.cursor()

    # Ejemplo de consulta
    mycursor.execute("SELECT * FROM placas")

    # Obtener resultados
    resultados = mycursor.fetchall()

    # Imprimir resultados
    for resultado in resultados:
        print(resultado)

    # Cerrar conexión
    conector.cerrar_conexion_db(mydb)
else:
    print("No se pudo establecer la conexión a la base de datos.")