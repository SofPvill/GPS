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

conn = odbc.connect(connection_string)
#print(conn)

# CONEXION
conn = odbc.connect(connection_string)

# SE CREA EL CURSOS 
cursor = conn.cursor()

# AQUI SE ESCRIBE LA INSTRUCCION DE SQL
sql_query = "SELECT * FROM Usuario"

# EJECUTAR LA INSTRUCCION
cursor.execute(sql_query)

# AGARRAR LOS RESULTADOS
results = cursor.fetchall()

# IMPRIMIR LOS RESULTADOS
for row in results:
    print(row)

# CIERRA EL CURSOS Y LA CONEXION
cursor.close()
conn.close()