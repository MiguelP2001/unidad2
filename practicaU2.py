import sqlite3

# Conectarse a la base de datos o crear una nueva si no existe
conexion = sqlite3.connect('basedatos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla llamada 'registros' con columnas para nombre, apellido y edad
cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                    nombre TEXT,
                    apellido TEXT,
                    edad INTEGER
                )''')

# Obtener los datos del usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))

# Insertar los datos en la tabla 'registros'
cursor.execute("INSERT INTO registros VALUES (?, ?, ?)", (nombre, apellido, edad))

# Guardar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()
