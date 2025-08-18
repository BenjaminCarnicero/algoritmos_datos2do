import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('servicio.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM pedidos")
registros = cursor.fetchall()

for fila in registros:
    print(fila)

conn.close()


# ========== BASE DE DATOS ==========
def crear_tabla():
    conn = sqlite3.connect('servicio.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            direccion TEXT,
            inconveniente TEXT,
            tecnico TEXT,
            fecha_visita TEXT,
            hora_visita TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insertar_pedido(cliente, direccion, inconveniente, tecnico, fecha, hora):
    conn = sqlite3.connect('servicio.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (cliente, direccion, inconveniente, tecnico, fecha_visita, hora_visita)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (cliente, direccion, inconveniente, tecnico, fecha, hora))
    conn.commit()
    conn.close()

# ========== LOGIN ==========
def verificar_login(usuario, clave):
    # Usuario fijo: admin / Clave fija: 1234
    return usuario == "Benjamin" and clave == "1234"

# ========== INTERFAZ PRINCIPAL ==========
def abrir_app():
    login.destroy()
    crear_tabla()
    root = tk.Tk()
    root.title("Repair Center - Pedidos de Servicio Técnico")

    # Etiquetas y campos
    tk.Label(root, text="Apellido y Nombre").grid(row=0, column=0)
    entry_cliente = tk.Entry(root, width=30)
    entry_cliente.grid(row=0, column=1)

    tk.Label(root, text="Dirección (Calle y altura)").grid(row=1, column=0)
    entry_direccion = tk.Entry(root, width=30)
    entry_direccion.grid(row=1, column=1)

    tk.Label(root, text="Inconveniente").grid(row=2, column=0)
    entry_inconveniente = tk.Entry(root, width=30)
    entry_inconveniente.grid(row=2, column=1)

    tk.Label(root, text="Técnico asignado").grid(row=3, column=0)
    entry_tecnico = tk.Entry(root, width=30)
    entry_tecnico.grid(row=3, column=1)

    tk.Label(root, text="Fecha (dd/mm/aaaa)").grid(row=4, column=0)
    entry_fecha = tk.Entry(root, width=30)
    entry_fecha.grid(row=4, column=1)

    tk.Label(root, text="Hora (hh:mm)").grid(row=5, column=0)
    entry_hora = tk.Entry(root, width=30)
    entry_hora.grid(row=5, column=1)

    def guardar():
        cliente = entry_cliente.get()
        direccion = entry_direccion.get()
        inconveniente = entry_inconveniente.get()
        tecnico = entry_tecnico.get()
        fecha = entry_fecha.get()
        hora = entry_hora.get()

        if not all([cliente, direccion, inconveniente, tecnico, fecha, hora]):
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return

        insertar_pedido(cliente, direccion, inconveniente, tecnico, fecha, hora)
        messagebox.showinfo("Éxito", "Pedido guardado correctamente.")
        entry_cliente.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_inconveniente.delete(0, tk.END)
        entry_tecnico.delete(0, tk.END)
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)

    tk.Button(root, text="Guardar Pedido", command=guardar).grid(row=6, column=0, columnspan=2, pady=10)

    root.mainloop()

# ========== LOGIN INTERFAZ ==========
login = tk.Tk()
login.title("Login - Repair Center")

tk.Label(login, text="Usuario").grid(row=0, column=0)
usuario = tk.Entry(login)
usuario.grid(row=0, column=1)

tk.Label(login, text="Contraseña").grid(row=1, column=0)
clave = tk.Entry(login, show="*")
clave.grid(row=1, column=1)

def entrar():
    if verificar_login(usuario.get(), clave.get()):
        abrir_app()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

tk.Button(login, text="Ingresar", command=entrar).grid(row=2, column=0, columnspan=2, pady=10)

login.mainloop()

