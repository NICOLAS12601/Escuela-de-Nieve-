import pyodbc as odbc

# Parámetros de conexión
DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'DESKTOP-GU5EMBG'
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

# Función para generar reporte de actividades con mayor ingreso
def reporte_actividades_mayor_ingreso():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            a.descripcion AS actividad,
            SUM(act.costo) AS ingresos_actividad,
            SUM(ISNULL(e.costo, 0)) AS ingresos_equipamiento,
            SUM(act.costo) + SUM(ISNULL(e.costo, 0)) AS ingresos_totales
        FROM actividades a
        JOIN clase c ON a.id = c.id_actividad
        JOIN alumno_clase ac ON c.id = ac.id_clase
        JOIN actividades act ON c.id_actividad = act.id
        LEFT JOIN equipamiento e ON ac.id_equipamiento = e.id
        GROUP BY a.descripcion
        ORDER BY ingresos_totales DESC
    """)
    data = cursor.fetchall()
    conn.close()
    return data


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
                LEFT JOIN alumno_clase ac ON ac.id_clase = c.id
            GROUP BY 
                a.descripcion
            ORDER BY 
                cantidad_alumnos DESC
        """)
        rows = cursor.fetchall()
        print("Datos retornados en reporte_actividades_mas_alumnos:", rows)
        return rows
    except odbc.Error as e:
        print("Error al generar el reporte:", e)
        return []
    finally:
        conn.close()

def reporte_turnos_mas_clases():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                CONCAT(CONVERT(VARCHAR(5), t.hora_inicio, 108), ' - ', CONVERT(VARCHAR(5), t.hora_fin, 108)) AS turno,
                COUNT(c.id) AS cantidad_clases
            FROM 
                clase c
                JOIN turnos t ON c.id_turno = t.id
            GROUP BY 
                CONVERT(VARCHAR(5), t.hora_inicio, 108), CONVERT(VARCHAR(5), t.hora_fin, 108)
            ORDER BY 
                cantidad_clases DESC
        """)
        rows = cursor.fetchall()
        print("Datos retornados en reporte_turnos_mas_clases:", rows)
        return rows
    except odbc.Error as e:
        print("Error al generar el reporte:", e)
        return []
    finally:
        conn.close()

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
    try:
        cursor.execute("DELETE FROM instructores WHERE ci = ?", (ci,))
        conn.commit()
        return "eliminado"
    except odbc.Error as e:
        print(f"Error al eliminar instructor: {e}")
        return "error"
    finally:
        conn.close()

    
# Función para obtener todos los turnos
def obtener_turnos():
    conn = conectar_bd()  
    cursor = conn.cursor()
    
    # Consulta SQL actualizada para seleccionar la columna 'id'
    cursor.execute("SELECT id, hora_inicio, hora_fin FROM turnos")
    
    # Recuperamos todos los registros
    turnos = cursor.fetchall()
    
    # Cerramos la conexión a la base de datos
    conn.close()
    
    return turnos

def agregar_turno(hora_inicio, hora_fin):
    conn = conectar_bd()
    cursor = conn.cursor()
    
    try:
        # Consulta para insertar un nuevo turno
        cursor.execute(
            "INSERT INTO turnos (hora_inicio, hora_fin) VALUES (?, ?)", 
            (hora_inicio, hora_fin)
        )
        conn.commit()  # Guardamos los cambios en la base de datos
        return "agregado"  # Indicamos que la operación fue exitosa
    except Exception as e:
        print(f"Error al agregar turno: {e}")
        return "error"  # Indicamos que ocurrió un error
    finally:
        conn.close()  # Cerramos la conexión a la base de datos

# Función para eliminar un turno
def eliminar_turno(turno_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM turnos WHERE id = ?", (turno_id,))
        conn.commit()
        return "eliminado"
    except odbc.Error as e:
        print(f"Error al eliminar turno: {e}")
        return "error"
    finally:
        conn.close()

# Función para buscar un turno por ID
def buscar_turno_por_id(cursor, turno_id):
    # Ejecutar la consulta para verificar si el turno existe
    query = "SELECT * FROM turnos WHERE id = ?"
    cursor.execute(query, (turno_id,))
    resultado = cursor.fetchone()
    
    # Si el resultado no es None, significa que el turno existe
    return resultado is not None

def obtener_actividades():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion, costo FROM actividades")
    actividades = cursor.fetchall()
    conn.close()
    return actividades

def agregar_actividad(descripcion, costo):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO actividades (descripcion, costo) VALUES (?, ?)",
            (descripcion, costo)
        )
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print("Error al agregar actividad:", e)
        return "error"
    finally:
        conn.close()

def eliminar_actividad(id):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM actividades WHERE id = ?", (id,))
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print(f"Error al eliminar actividad: {e}")
        return "error"
    finally:
        conn.close()

def obtener_alumnos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT ci, nombre, apellido, telefono, correo FROM alumnos")
    alumnos = cursor.fetchall()
    conn.close()
    return alumnos

def agregar_alumno(ci, nombre, apellido, telefono, correo):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO alumnos (ci, nombre, apellido, telefono, correo)
            VALUES (?, ?, ?, ?, ?)
        """, (ci, nombre, apellido, telefono, correo))
        conn.commit()
        return "ok"
    except odbc.IntegrityError:
        return "existe"
    except Exception as e:
        print(f"Error al agregar alumno: {e}")
        return "error"
    finally:
        conn.close()

def eliminar_alumno(ci):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM alumnos WHERE ci = ?", (ci,))
        conn.commit()
        return "ok"
    except odbc.IntegrityError:
        return "referenciado"  # Si el alumno está en uso en otras tablas
    finally:
        conn.close()

# Función para agregar una nueva clase
def agregar_clase(ci_instructor, id_actividad, id_turno):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clase (ci_instructor, id_actividad, id_turno)
            VALUES (?, ?, ?)
        """, (ci_instructor, id_actividad, id_turno))
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print("Error al agregar clase:", e)
        return "error"
    finally:
        conn.close()

def obtener_clases():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            c.id,
            i.nombre AS instructor_nombre,
            i.apellido AS instructor_apellido,
            a.descripcion AS actividad_descripcion,
            t.hora_inicio,
            t.hora_fin
        FROM 
            clase c
            JOIN instructores i ON c.ci_instructor = i.ci
            JOIN actividades a ON c.id_actividad = a.id
            JOIN turnos t ON c.id_turno = t.id
    """)
    # Obtener los nombres de las columnas
    columns = [column[0] for column in cursor.description]
    clases = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return clases

def eliminar_clase(clase_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clase WHERE id = ?", (clase_id,))
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print("Error al eliminar la clase:", e)
        return "error"
    finally:
        conn.close()
        
def obtener_inscripciones():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            i.id_clase,
            i.ci_alumno,
            a.nombre AS alumno_nombre,
            a.apellido AS alumno_apellido,
            act.descripcion AS actividad_descripcion,
            inst.nombre AS instructor_nombre,
            inst.apellido AS instructor_apellido,
            t.hora_inicio,
            t.hora_fin,
            e.descripcion AS equipamiento_descripcion,
            i.alquiler
        FROM alumno_clase i
        JOIN alumnos a ON i.ci_alumno = a.ci
        JOIN clase c ON i.id_clase = c.id
        JOIN actividades act ON c.id_actividad = act.id
        JOIN instructores inst ON c.ci_instructor = inst.ci
        JOIN turnos t ON c.id_turno = t.id
        LEFT JOIN equipamiento e ON i.id_equipamiento = e.id
    """)
    columns = [column[0] for column in cursor.description]
    inscripciones = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return inscripciones

def agregar_inscripcion(id_clase, ci_alumno, id_equipamiento, alquiler):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento, alquiler) VALUES (?, ?, ?, ?)",
            (id_clase, ci_alumno, id_equipamiento, alquiler)
        )
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print("Error al agregar inscripción:", e)
        return "error"
    finally:
        conn.close()

def eliminar_inscripcion(clase_id, ci_alumno):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            DELETE FROM alumno_clase 
            WHERE id_clase = ? AND ci_alumno = ?
        """, (clase_id, ci_alumno))
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print("Error al eliminar inscripción:", e)
        return "error"
    finally:
        conn.close()

# Función para validar las credenciales de usuario
def validate_user(correo, contrasena):
    # Conexión a la base de datos SQLite
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "SELECT * FROM login WHERE correo = ? AND contrasena = ?"
    cursor.execute(query, (correo, contrasena))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def obtener_equipamientos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            e.id,
            e.descripcion,
            e.costo,
            a.descripcion AS actividad_descripcion
        FROM equipamiento e
        JOIN actividades a ON e.id_actividad = a.id
    """)
    equipamientos = cursor.fetchall()
    conn.close()
    return equipamientos

def agregar_equipamiento(descripcion, costo, id_actividad):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO equipamiento (descripcion, costo, id_actividad) VALUES (?, ?, ?)",
            (descripcion, costo, id_actividad)
        )
        conn.commit()
        return "ok"
    except odbc.Error as e:
        print("Error al agregar equipamiento:", e)
        return "error"
    finally:
        conn.close()

def eliminar_equipamiento(id_equipamiento):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM equipamiento WHERE id = ?", (id_equipamiento,))
        conn.commit()
        return "ok"
    except odbc.Error as e:
        # Obtener el número de error
        error_code = e.args[0]
        if error_code == '23000':
            # Código de error de violación de restricción de clave foránea
            print("Error al eliminar equipamiento:", e)
            return "referenciado"
        else:
            print("Error al eliminar equipamiento:", e)
            return "error"
    finally:
        conn.close()

def obtener_actividad_de_clase(id_clase):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_actividad FROM clase WHERE id = ?", (id_clase,))
        result = cursor.fetchone()
        return result[0] if result else None
    except odbc.Error as e:
        print("Error al obtener actividad de la clase:", e)
        return None
    finally:
        conn.close()

def obtener_actividad_de_equipamiento(id_equipamiento):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_actividad FROM equipamiento WHERE id = ?", (id_equipamiento,))
        result = cursor.fetchone()
        return result[0] if result else None
    except odbc.Error as e:
        print("Error al obtener actividad del equipamiento:", e)
        return None
    finally:
        conn.close()

def obtener_equipamientos_por_actividad(id_actividad):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                e.id,
                e.descripcion,
                e.costo,
                a.descripcion AS actividad_descripcion
            FROM equipamiento e
            JOIN actividades a ON e.id_actividad = a.id
            WHERE e.id_actividad = ?
        """, (id_actividad,))
        equipamientos = cursor.fetchall()
        return equipamientos
    except odbc.Error as e:
        print("Error al obtener equipamientos por actividad:", e)
        return []
    finally:
        conn.close()
