
# Importamos las herramientas que vamos a usar
import pandas as pd                  # para manejar los datos en tabla
import matplotlib.pyplot as plt      # para hacer el gráfico
import os                            # para crear carpetas

# ── 1. CARGAMOS LOS DATOS ──────────────────────────────────────────
df = pd.read_csv("datos/dataset_climatico.csv")

# Mostramos las primeras filas para ver cómo son los datos
print("Primeras filas del dataset:")
print(df.head())

# ── 2. CALCULAMOS INDICADORES BÁSICOS ─────────────────────────────
promedio = df["Mean"].mean()
maximo   = df["Mean"].max()
minimo   = df["Mean"].min()

print("\n--- Resultados ---")
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Temperatura máxima:   {maximo:.2f} °C")
print(f"Temperatura mínima:   {minimo:.2f} °C")

# ── 3. HACEMOS EL GRÁFICO ─────────────────────────────────────────
# Creamos la carpeta /resultados si no existe
os.makedirs("resultados", exist_ok=True)

# Dibujamos la línea de temperatura a lo largo del tiempo
plt.figure(figsize=(12, 5))
plt.plot(df["Mean"].values, color="tomato", linewidth=1)

# Títulos y etiquetas
plt.title("Evolución de la temperatura global")
plt.xlabel("Meses registrados")
plt.ylabel("Anomalía de temperatura (°C)")

# Guardamos el gráfico como imagen
plt.tight_layout()
plt.savefig("resultados/grafico_temperatura.png")
plt.show()

print("\nGráfico guardado en /resultados/grafico_temperatura.png")
