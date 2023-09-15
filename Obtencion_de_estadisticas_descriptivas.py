# Importar las bibliotecas necesarias
import pandas as pd
import random
import numpy as np

# Carga los datos y aplica las conversiones de unidades
df = pd.read_csv("peso_estatura_genero.csv")
df.Estatura = df.Estatura * 2.54  # Convertir de pulgadas a cm
df.Peso = df.Peso / 2.2  # Convertir de libras a kg

# Información básica del conjunto de datos
print("Información básica del conjunto de datos:")
print(df.info())
print()

# Resumen estadístico y rangos de las variables
print("Resumen estadístico:")
print(df.describe())
print()

# Media Recortada
sorted_df = df["Estatura"].sort_values()
sorted_df = sorted_df.reset_index(drop=True)
p = 5
mean_recort = sorted_df[p:-p].mean()
print(f"Media recortada de la estatura: {mean_recort}")

# Media Ponderada
weights = [random.random() for i in range(len(df))]
media_pond = np.average(df["Estatura"], weights=weights)
print(f"Media ponderada de la estatura: {media_pond}")

# Moda
moda = df["Estatura"].mode()[0]
print(f"Moda de la estatura: {moda}")

# Mediana
mediana = df["Estatura"].median()
print(f"Mediana de la estatura: {mediana}")

# Varianza
varianza = df["Estatura"].var()
print(f"Varianza de la estatura: {varianza}")

# Desviación estándar
desv_est = df["Estatura"].std()
print(f"Desviación estándar de la estatura: {desv_est}")

# Cuartiles
cuartiles = df["Estatura"].quantile([0.25, 0.5, 0.75])
print(f"Cuartiles de la estatura: {cuartiles}")