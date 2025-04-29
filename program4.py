import tkinter as tk
import random

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Memoria - Armar Parejas")

# Configuración del tablero
filas, columnas = 4, 4  # Cambiado a un tablero 4x4 para garantizar un número par de casillas
total_casillas = filas * columnas

# Generar pares de números y mezclarlos
numeros = list(range(1, (total_casillas // 2) + 1)) * 2
random.shuffle(numeros)

# Variables para el juego
botones = []
primer_boton = None
segundo_boton = None
pares_encontrados = 0

def revelar_boton(boton, fila, columna):
    global primer_boton, segundo_boton, pares_encontrados

    # Revelar el número del botón
    boton.config(text=numeros[fila * columnas + columna], state="disabled")

    # Verificar si es el primer o segundo botón seleccionado
    if not primer_boton:
        primer_boton = (boton, fila, columna)
    elif not segundo_boton:
        segundo_boton = (boton, fila, columna)

        # Comparar los dos botones seleccionados
        if numeros[primer_boton[1] * columnas + primer_boton[2]] == numeros[segundo_boton[1] * columnas + segundo_boton[2]]:
            # Si coinciden, mantenerlos deshabilitados
            primer_boton[0].config(state="disabled", bg="lightgreen")
            segundo_boton[0].config(state="disabled", bg="lightgreen")
            pares_encontrados += 1
            primer_boton = None
            segundo_boton = None

            # Verificar si el juego ha terminado
            if pares_encontrados == total_casillas // 2:
                tk.messagebox.showinfo("¡Felicidades!", "¡Has encontrado todas las parejas!")
        else:
            # Si no coinciden, ocultarlos después de un breve retraso
            ventana.after(1000, ocultar_botones)

def ocultar_botones():
    global primer_boton, segundo_boton
    # Ocultar los botones seleccionados
    if primer_boton and segundo_boton:
        primer_boton[0].config(text="", state="normal", bg="SystemButtonFace")
        segundo_boton[0].config(text="", state="normal", bg="SystemButtonFace")
    primer_boton = None
    segundo_boton = None

# Crear los botones del tablero
for fila in range(filas):
    for columna in range(columnas):
        boton = tk.Button(ventana, text="", width=6, height=3, font=("Arial", 14),
                          command=lambda f=fila, c=columna: revelar_boton(botones[f * columnas + c], f, c))
        boton.grid(row=fila, column=columna, padx=5, pady=5)
        botones.append(boton)

# Iniciar el bucle principal de la ventana
ventana.mainloop()