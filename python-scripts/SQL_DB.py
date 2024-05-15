import pypyodbc as odbc  # pip install pypyodbc

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'LAPTOP-P45GKG6I'
DATABASE_NAME = 'APPGPS'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid = sa;
    pwd = Emi7337175.;
"""

# CONEXION
conn = odbc.connect(connection_string)

# SE CREA EL CURSOS 
cursor = conn.cursor()

#----------------PARA PODER LEER DATOS DE LA BASE DE DATOS

# AQUI SE ESCRIBE LA INSTRUCCION DE SQL
#Instrucciones SELECT
#sql_query = "SELECT * FROM Usuario"

# EJECUTAR LA INSTRUCCION
#cursor.execute(sql_query)

# AGARRAR LOS RESULTADOS
#results = cursor.fetchall()

# IMPRIMIR LOS RESULTADOS
#for row in results:
#    print(row)

#----------------MANIPULAR DATOS EN LA BASE DE DATOS

#Instrucciones de INSERT, UPDATE y DELETE
sql_query = "insert into Usuario (idUsuario, Nombre, Rol, Contrasena) values ('2222', 'Pepe', 'Admin', '1234')"

# EJECUTAR LA INSTRUCCION
cursor.execute(sql_query)

#GUARDAR LOS CAMBIOS HECHOS
conn.commit()

#-- CIERRA EL CURSOS Y LA CONEXION
cursor.close()
conn.close()