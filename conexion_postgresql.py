import psycopg2


def conectar_db():
    try: 
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='root',
            database='reporteAutomatico',
        )
        print("Conexion correcta")
        return connection
    except Exception as ex:
        print(ex)
        return None




def buscarUsuario(connection,usuario, password):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s ", (usuario,))

        rows=cursor.fetchall()

        if not rows:
            mensaje = "Usuario no encontrado"
        else:
            for row in rows:
                stored_password = row[2]
                if stored_password == password :
                    mensaje = "login"
                else:
                    mensaje = "Password incorrecta"

        print(mensaje)  
        return mensaje
        
    except Exception as ex:
        print(ex)