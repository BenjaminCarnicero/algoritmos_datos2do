### Calculadora probada con POO. 

import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora POO - AyED II")
        master.geometry("300x250")

        # Entradas
        tk.Label(master, text="Número 1:").pack()
        self.entrada1 = tk.Entry(master)
        self.entrada1.pack()

        tk.Label(master, text="Número 2:").pack()
        self.entrada2 = tk.Entry(master)
        self.entrada2.pack()

        # Botones
        tk.Button(master, text="Sumar", command=self.sumar).pack(pady=2)
        tk.Button(master, text="Restar", command=self.restar).pack(pady=2)
        tk.Button(master, text="Multiplicar", command=self.multiplicar).pack(pady=2)
        tk.Button(master, text="Dividir", command=self.dividir).pack(pady=2)

        # Resultado
        self.resultado_label = tk.Label(master, text="Resultado:")
        self.resultado_label.pack(pady=10)

    def obtener_valores(self):
        try:
            n1 = float(self.entrada1.get())
            n2 = float(self.entrada2.get())
            return n1, n2
        except ValueError:
            messagebox.showerror("Error", "Ingresá solo números")
            return None, None

    def sumar(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.resultado_label.config(text=f"Resultado: {n1 + n2}")

    def restar(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.resultado_label.config(text=f"Resultado: {n1 - n2}")

    def multiplicar(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            self.resultado_label.config(text=f"Resultado: {n1 * n2}")

    def dividir(self):
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            if n2 != 0:
                self.resultado_label.config(text=f"Resultado: {n1 / n2}")
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
