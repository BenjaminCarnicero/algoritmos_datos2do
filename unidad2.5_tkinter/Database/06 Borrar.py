import sqlite3

conexion=sqlite3.connect("bd1.db")
conexion.execute("delete from articulos where codigo=1 ")
conexion.commit()
conexion.close()