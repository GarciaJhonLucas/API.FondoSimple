import sqlite3
conexion=sqlite3.connect("fondo_simple.db")
try:
    conexion.execute("""create table clientes (
                              id integer primary key autoincrement,
                              nombres text,
                              apellido_paterno text,
                              apellido_materno text,
                              numero_documento text,
                              direccion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    
conexion.close()