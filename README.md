# loginPythonPostgres
#Codigo creado por Alan Contreras, 

Se debe instalar postgreSQL, pgadmin4 o psql 
Posteriormente, crear una base con las siguientes especificaciones (NOTA: deben coincidir ambas configuraciones {postgreSQL.py, basePostgres}

database="login_base",
user="postgres",
password="12345678",
host="localhost",  # Cambia esto si tu base de datos no está en localhost
port="5432"  

Una vez hecho, crear una tabla llamada usuarios con (usuarioId, username, contraseña)
Llenar la base como desee

Al correr el código python pedirá algún usuario de la tabla usuarios con su respectiva contraseña

Si se comete un error 3 veces, se termina el programa. 
