import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    dato_extra = entry_dato_extra.get()
    
    # Validar que los campos no estén vacíos
    if not nombre or not apellido or not edad or not dato_extra:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        return
    
    # Mostrar los datos en un cuadro de mensaje
    datos = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDato Extra: {dato_extra}"
    messagebox.showinfo("Datos Ingresados", datos)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Datos")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Edad:").grid(row=2, column=0, padx=10, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Dato Extra:").grid(row=3, column=0, padx=10, pady=5)
entry_dato_extra = tk.Entry(ventana)
entry_dato_extra.grid(row=3, column=1, padx=10, pady=5)

# Botón para mostrar los datos
btn_mostrar = tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos)
btn_mostrar.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()