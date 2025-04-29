import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt
import numpy as np

def click_boton(valor):
    entrada_texto.set(entrada_texto.get() + str(valor))

def limpiar():
    entrada_texto.set("")

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", "Expresión inválida")

def funcion_cientifica(func):
    try:
        valor = float(entrada_texto.get())
        if func == "sin":
            resultado = math.sin(math.radians(valor))
        elif func == "cos":
            resultado = math.cos(math.radians(valor))
        elif func == "tan":
            resultado = math.tan(math.radians(valor))
        elif func == "log":
            resultado = math.log10(valor)
        elif func == "exp":
            resultado = math.exp(valor)
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", "Entrada inválida")

def graficar_funcion(func):
    try:
        x = np.linspace(-360, 360, 1000)  # Rango de valores para x
        if func == "sin":
            y = np.sin(np.radians(x))
        elif func == "cos":
            y = np.cos(np.radians(x))
        elif func == "tan":
            y = np.tan(np.radians(x))
            y[np.abs(y) > 10] = np.nan  # Limitar valores extremos de tangente
        else:
            raise ValueError("Función no soportada para graficar")

        # Crear la gráfica
        plt.figure(figsize=(8, 4))
        plt.plot(x, y, label=f"{func}(x)")
        plt.title(f"Gráfica de {func}(x)")
        plt.xlabel("x (grados)")
        plt.ylabel(f"{func}(x)")
        plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
        plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo graficar: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")

# Variable para la entrada de texto
entrada_texto = tk.StringVar()

# Campo de entrada
entrada = tk.Entry(ventana, textvariable=entrada_texto, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
entrada.grid(row=0, column=0, columnspan=4)

# Botones de números y operaciones básicas
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+"
]

fila = 1
columna = 0

for boton in botones:
    if boton == "C":
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 14), command=limpiar).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 14), command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón de igual
tk.Button(ventana, text="=", padx=20, pady=20, font=("Arial", 14), command=calcular).grid(row=fila, column=0, columnspan=4)

# Botones de funciones científicas
funciones = ["sin", "cos", "tan", "log", "exp"]
fila += 1
columna = 0

for funcion in funciones:
    tk.Button(ventana, text=funcion, padx=20, pady=20, font=("Arial", 14), command=lambda f=funcion: funcion_cientifica(f)).grid(row=fila, column=columna)
    columna += 1

# Botones para graficar funciones
fila += 1
columna = 0
for funcion in ["sin", "cos", "tan"]:
    tk.Button(ventana, text=f"Graficar {funcion}", padx=10, pady=20, font=("Arial", 12), command=lambda f=funcion: graficar_funcion(f)).grid(row=fila, column=columna)
    columna += 1

# Iniciar el bucle principal de la ventana
ventana.mainloop()