import tkinter as tk
import random
from tkinter import messagebox

class JuegoParejas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Parejas 5x5")

        # Crear una lista de 12 pares + 1 comodín
        valores = list("ABCDEFGHIJKLM"[:12]) * 2 + ["*"]  # 25 en total
        random.shuffle(valores)

        self.botones = []
        self.valores = {}
        self.revelados = {}
        self.seleccion = []

        # Crear botones
        for i in range(5):
            fila = []
            for j in range(5):
                idx = i * 5 + j
                valor = valores[idx]
                btn = tk.Button(root, text=" ", width=6, height=3,
                                command=lambda i=i, j=j: self.revelar(i, j))
                btn.grid(row=i, column=j)
                fila.append(btn)
                self.valores[(i, j)] = valor
            self.botones.append(fila)

    def revelar(self, i, j):
        if (i, j) in self.revelados or (i, j) in self.seleccion:
            return

        btn = self.botones[i][j]
        btn.config(text=self.valores[(i, j)], state="disabled")
        self.seleccion.append((i, j))

        if len(self.seleccion) == 2:
            self.root.after(1000, self.comprobar_pareja)

    def comprobar_pareja(self):
        (i1, j1), (i2, j2) = self.seleccion
        v1 = self.valores[(i1, j1)]
        v2 = self.valores[(i2, j2)]

        if v1 == v2:
            self.revelados[(i1, j1)] = True
            self.revelados[(i2, j2)] = True
        else:
            self.botones[i1][j1].config(text=" ", state="normal")
            self.botones[i2][j2].config(text=" ", state="normal")

        self.seleccion.clear()

        if len(self.revelados) == 24:  # 12 parejas * 2
            messagebox.showinfo("¡Felicidades!", "¡Has encontrado todas las parejas!")

# Ejecutar juego
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoParejas(root)
    root.mainloop()
