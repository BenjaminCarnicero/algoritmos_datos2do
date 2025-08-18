## Calculadora funcional

import tkinter as tk
from tkinter import messagebox

def operar(op):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())

        if op == '+':
            resultado = n1 + n2
        elif op == '-':
            resultado = n1 - n2
        elif op == '*':
            resultado = n1 * n2
        elif op == '/':
            if n2 != 0:
                resultado = n1 / n2
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return

        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Ingresá solo números")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora - AyED II")
ventana.geometry("300x250")

# Entradas
tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botones de operaciones
tk.Button(ventana, text="Sumar", command=lambda: operar('+')).pack(pady=2)
tk.Button(ventana, text="Restar", command=lambda: operar('-')).pack(pady=2)
tk.Button(ventana, text="Multiplicar", command=lambda: operar('*')).pack(pady=2)
tk.Button(ventana, text="Dividir", command=lambda: operar('/')).pack(pady=2)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
