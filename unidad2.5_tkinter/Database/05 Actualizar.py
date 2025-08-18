import sqlite3

conexion=sqlite3.connect("bd1.db")
conexion.execute("update articulos set descripcion = 'uva' where codigo=2 ")
conexion.commit()
conexion.close()