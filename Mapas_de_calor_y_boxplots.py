import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Cargar el conjunto de datos
df = pd.read_csv("clientes-centro-comercial.csv")

# Descripción general de los datos
print(df.head())
print(df.describe())

# Diagrama de cajas y bigotes para cada columna numérica
numeric_columns = df.select_dtypes(include=[np.number]).columns
for column in numeric_columns:
    plt.figure()
    sns.boxplot(data=df, y=column)
    plt.title(f"Diagrama de caja y bigotes para {column}")
    plt.show()

# Histogramas para cada columna numérica
for column in numeric_columns:
    plt.figure()
    sns.histplot(data=df, x=column, bins=20, kde=True)
    plt.title(f"Histograma para {column}")
    plt.show()

# Mapa de calor para la matriz de correlación
corr = df[numeric_columns].corr()
plt.figure()
sns.heatmap(data=corr, vmin=-1, vmax=1, cmap="coolwarm", annot=True)
plt.title("Mapa de calor para la matriz de correlación")
plt.show()