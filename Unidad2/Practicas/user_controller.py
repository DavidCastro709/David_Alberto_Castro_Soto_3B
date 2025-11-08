from database import crear_conexion

def ver_usuarios():
    conexion = crear_conexion()
    if not conexion:
        return []
    
    cursor = conexion.cursor()
    cursor.execute("SELECT id, usuario FROM e")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def agregar_usuarios(username, password):
    conexion = crear_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO e (usuario, password) VALUES (%s, %s)", (username, password))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear un usuario. Tipo de error {e}")
        return False
        return False
    
def  actualizar_usuario(id_usuario, new_usuario, new_pasword):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE e SET usuario = %s, password = %s WHERE id_usuario = %s"),(new_pasword, new_pasword,id_usuario)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error al actualizar usuario. Tipo de error: {e}")

def eliminar_usuario(id_usuario):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM e WHERE id = %s",(id_usuario))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print("Error al eliminar usuario. Tipo de error: {e}")
        return False
       



