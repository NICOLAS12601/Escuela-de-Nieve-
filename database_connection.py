import pyodbc as odbc

# Parámetros de conexión
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'PCNICO'
DATABASE_NAME = 'EscuelaNieve'

# Cadena de conexión
connection_string = f"""
    DRIVER={{SQL Server}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""

# Función para conectar a la base de datos
def conectar_bd():
    try:
        connection = odbc.connect(connection_string)
        print("Conexión exitosa a la base de datos.")
        return connection
    except odbc.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Función para agregar un alumno
def agregar_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, correo)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (ci, nombre, apellido, fecha_nacimiento, telefono, correo))
        conn.commit()
        print("Alumno agregado exitosamente.")
    except odbc.Error as e:
        print("Error al agregar alumno:", e)
    finally:
        if 'conn' in locals():
            conn.close()

# Función para generar reporte de actividades con mayor ingreso
def reporte_actividades_mayor_ingreso():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                a.descripcion AS actividad,
                SUM(a.costo + COALESCE(e.costo, 0)) AS ingresos_totales
            FROM 
                clase c
                JOIN actividades a ON c.id_actividad = a.id
                LEFT JOIN alumno_clase ac ON ac.id_clase = c.id
                LEFT JOIN equipamiento e ON ac.id_equipamiento = e.id
            GROUP BY 
                a.descripcion
            ORDER BY 
                ingresos_totales DESC
        """)
        rows = cursor.fetchall()
        print("Datos obtenidos del reporte:", rows)  # Verifica que los datos se obtienen
        return rows
    except odbc.Error as e:
        print("Error al generar el reporte:", e)
        return []
    finally:
        if 'conn' in locals():
            conn.close()

def reporte_actividades_mas_alumnos():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                a.descripcion AS actividad,
                COUNT(ac.ci_alumno) AS cantidad_alumnos
            FROM 
                clase c
                JOIN actividades a ON c.id_actividad = a.id
                JOIN alumno_clase ac ON ac.id_clase = c.id
            GROUP BY 
                a.descripcion
            ORDER BY 
                cantidad_alumnos DESC
        """)
        rows = cursor.fetchall()
        return rows
    except odbc.Error as e:
        print("Error al generar el reporte:", e)
        return []
    finally:
        if 'conn' in locals():
            conn.close()

def reporte_turnos_mas_clases():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                t.hora_inicio,
                t.hora_fin,
                COUNT(c.id) AS cantidad_clases
            FROM 
                clase c
                JOIN turnos t ON c.id_turno = t.id
            GROUP BY 
                t.hora_inicio, t.hora_fin
            ORDER BY 
                cantidad_clases DESC
        """)
        rows = cursor.fetchall()
        return rows
    except odbc.Error as e:
        print("Error al generar el reporte:", e)
        return []
    finally:
        if 'conn' in locals():
            conn.close()

# Ejemplo de uso de la conexión para ejecutar una consulta de prueba
try:
    conn = conectar_bd()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipamiento")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except odbc.Error as e:
    print("Error al conectar o ejecutar la consulta de prueba:", e)
finally:
    if 'conn' in locals():
        conn.close()
        print("Conexión cerrada.")

# Función para obtener todos los instructores
def obtener_instructores():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT ci, nombre, apellido FROM instructores")
    instructores = cursor.fetchall()
    conn.close()
    return instructores

# Función para agregar un instructor, retorna "existe" si ya hay un instructor con esa CI
def agregar_instructor(ci, nombre, apellido):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO instructores (ci, nombre, apellido) VALUES (?, ?, ?)", (ci, nombre, apellido))
        conn.commit()
        return "ok"
    except odbc.IntegrityError:
        return "existe"
    finally:
        conn.close()

# Función para eliminar un instructor por CI
def eliminar_instructor(ci):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM instructores WHERE ci = ?", (ci,))
    conn.commit()
    conn.close()
    
# Función para obtener todos los turnos
def obtener_turnos():
    conn = conectar_bd()  # Asegúrate de que conectar_bd() esté correctamente definida
    cursor = conn.cursor()
    
    # Consulta SQL actualizada para seleccionar la columna 'id'
    cursor.execute("SELECT id, hora_inicio, hora_fin FROM turnos")
    
    # Recuperamos todos los registros
    turnos = cursor.fetchall()
    
    # Cerramos la conexión a la base de datos
    conn.close()
    
    return turnos

