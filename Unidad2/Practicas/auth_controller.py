#Controlador responsable de la logica de autenticacion.
#Separa la logica del Login para mantener limpio el codigo de la interfaz.

from database import crear_conexion

def validar_credenciales(usuario,password):
    conexion=crear_conexion()
    if not conexion:
        return False

    cursor=conexion.cursor()
    consulta="SELECT * FROM e WHERE usuario=%s AND password=%s"
    cursor.execute(consulta,(usuario,password))
    result=cursor.fetchone()

    conexion.close()
    return bool(result)

