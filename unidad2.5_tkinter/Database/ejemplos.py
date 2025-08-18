# from tkinter import *
# from tkinter import ttk

# root = Tk()
# notebook = ttk.Notebook(root)
# frame1 = Frame(notebook)
# frame2 = Frame(notebook)

# notebook.add(frame1, text="Pestaña 1")
# notebook.add(frame2, text="Pestaña 2")
# notebook.pack()

# root.mainloop()


#########
from tkinter import *
from tkinter import ttk

root = Tk()
menubar = Menu(root)

archivo = Menu(menubar, tearoff=0)
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_separator()
archivo.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Archivo", menu=archivo)
root.config(menu=menubar)

root.mainloop()



def saludar():
    print("Hola!")

boton = Button(root, text="Saludar", command=saludar)


#
def presionar_tecla(event):
    print(f"Presionaste: {event.char}")

root.bind("<Key>", presionar_tecla)


# INSERT

cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Lucas", 30))
conexion.commit()

# UPDATE

cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (31, "Lucas"))
conexion.commit()

Busca al usuario que se llama "Lucas" y le actualiza la edad a 31.
UPDATE se usa para modificar datos ya existentes. El commit() guarda el cambio.

# DELETE

cursor.execute("DELETE FROM usuarios WHERE nombre = ?", ("Lucas",))
conexion.commit()