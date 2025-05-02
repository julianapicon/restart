import csv
import random
import datetime
import matplotlib.pyplot as plt
from collections import Counter

# Paso 1: Generar CSV con datos aleatorios de insulina para 30 días
def generar_csv(nombre_archivo="insulina_mensual.csv"):
    hoy = datetime.date.today()
    fechas = [hoy - datetime.timedelta(days=i) for i in range(29, -1, -1)]
    with open(nombre_archivo, mode="w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["fecha", "insulina"])
        for fecha in fechas:
            nivel = round(random.uniform(2, 60), 1)  # valores entre 2 y 60 µU/mL
            writer.writerow([fecha, nivel])

# Paso 2: Clasificar valores de insulina
def clasificar_insulina(valor):
    if valor < 2:
        return "Muy bajo"
    elif 2 <= valor < 25:
        return "Normal"
    elif 25 <= valor < 50:
        return "Elevado"
    else:
        return "Muy alto"

# Paso 3: Leer CSV y analizar los datos
def analizar_insulina(nombre_archivo="insulina_mensual.csv"):
    resultados = []
    with open(nombre_archivo, mode="r") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            fecha = fila["fecha"]
            valor = float(fila["insulina"])
            clasificacion = clasificar_insulina(valor)
            resultados.append((fecha, valor, clasificacion))
    return resultados

# Paso 4: Resumen y gráfica
def mostrar_resultados(resultados):
    conteo = Counter([r[2] for r in resultados])
    print("\nResumen de Clasificaciones:")
    for clasificacion, cantidad in conteo.items():
        print(f"{clasificacion}: {cantidad} casos")

    fechas = [r[0] for r in resultados]
    valores = [r[1] for r in resultados]
    
    plt.figure(figsize=(12, 6))
    plt.plot(fechas, valores, marker="o")
    plt.xticks(rotation=45)
    plt.title("Niveles de Insulina Diarios (µU/mL)")
    plt.xlabel("Fecha")
    plt.ylabel("Insulina")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Ejecutar flujo principal
generar_csv()
datos = analizar_insulina()
mostrar_resultados(datos)
