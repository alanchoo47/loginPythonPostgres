#importar bibliotecas
import psycopg2
import getpass

#Se hace la conexión hacia la base de Datos de postgres, si es exitoso regresa el objeto de conexion
def conexionBaseDatos():
    try:
        #Se insertan los datos de la base de datos
        conn = psycopg2.connect(
            database="login_base",
            user="postgres",
            password="12345678",
            host="localhost",  # Cambia esto si tu base de datos no está en localhost
            port="5432"         # Puerto predeterminado de PostgreSQL
        )
        return conn
    #Si hay error al conectar a la base de datos, imprime el siguiente mensaje y regresa None
    except Exception as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
        return None

#Función para identificar 
def login(intentos):

    #Solicita usuario y contraseña
    usuario = input("Nombre de usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    
    #Realiza una conexion a la base de datos usando la funcion conexionBaseDatos
    conn = conexionBaseDatos()


    if conn is not None:
        #se crear un cursor para ejecutar consultas SQL 
        cursor = conn.cursor()
        #ejecuta un comando especifico
        cursor.execute("SELECT usuario_id FROM usuarios WHERE username = %s AND contraseña = %s", (usuario, contraseña))
        #Obtiene el resultado de la consulta
        user_id = cursor.fetchone()
        #Cierra la conexion a la base de datos
        conn.close()
        
        if user_id:
            print("Inicio de sesión exitoso. Bienvenido, " + usuario + "!")
            intentos = -10
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            intentos -= 1
    return intentos


if __name__ == "__main__":
    #Se darán intentos definidos por la variable intentos
    intentos  = 3
    #El programa se detendrá hasta que se acaben los intentos
    while intentos > 0 :
        intentos = login(intentos) 
    if intentos == 0:
        print("Ha alcanzado el numero maximo de intentos, vuelva a correr el programa")
    elif intentos == 10:
        print(" ")
