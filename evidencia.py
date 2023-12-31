#Evidencia
#Integrantes:
#Luis Omar Olmedo
#Diego Ivan Morales
#Milan De Alba

# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carga los datos
df = pd.read_csv("data.csv")

# Información básica y estadísticas descriptivas
print("Información básica del conjunto de datos:")
print(df.info())
print()
print("Resumen estadístico:")
print(df.describe())
print()

# Media recortada para la columna 'Value'
sorted_df = df['Value'].sort_values()
sorted_df = sorted_df.reset_index(drop=True)
p = 5
mean_recort = sorted_df[p:-p].mean()
print(f"Media recortada de la densidad de servidores: {mean_recort}")

# Cambio de densidad de servidores en México con respecto al tiempo
mexico_data = df[df['Country Name'] == 'Mexico']
plt.figure()
sns.lineplot(x='Year', y='Value', data=mexico_data, label='México')
sns.lineplot(x='Year', y='Value', data=df, label='Promedio Mundial')
plt.title('Cambio en la Densidad de Servidores en México vs Promedio Mundial')
plt.xlabel('Año')
plt.ylabel('Densidad de Servidores')
plt.legend()
plt.show()

# Densidad de servidores en el último año registrado para varios países (Top 10)
latest_year = df['Year'].max()
latest_data = df[df['Year'] == latest_year]
top_countries_latest = latest_data.groupby('Country Name')['Value'].mean().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(y=top_countries_latest.index, x=top_countries_latest.values, orient='h')
plt.title(f'Top 10 Países por Densidad de Servidores en {latest_year}')
plt.xlabel('Densidad de Servidores')
plt.ylabel('País')
plt.show()

# Gráfica de pastel para comparar British Virgin Islands, Liechtenstein y Gibraltar en el último año
latest_year = df['Year'].max()
selected_countries = df[(df['Country Name'].isin(['British Virgin Islands', 'Liechtenstein', 'Gibraltar'])) & (df['Year'] == latest_year)]
plt.figure()
plt.pie(selected_countries['Value'], labels=selected_countries['Country Name'], autopct='%1.1f%%')
plt.title(f'Distribución de la Densidad de Servidores en el Año {latest_year} entre British Virgin Islands, Liechtenstein y Gibraltar')
plt.show()

# Mapa de calor vertical de la densidad de servidores en la Unión Europea a lo largo de los años
eu_data = df[df['Country Name'] == 'European Union']
plt.figure(figsize=(10, 8))
heatmap_data = eu_data.pivot_table(values='Value', index='Year', columns='Country Name')
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor de la Densidad de Servidores en la Unión Europea')
plt.xlabel('Unión Europea')
plt.ylabel('Año')
plt.gca().invert_yaxis()
plt.show()

from scipy.stats import linregress

# Filtrar datos para incluir solo las regiones de interés
regions_of_interest = ['Latin America & Caribbean', 'Europe & Central Asia']
filtered_data = df[df['Country Name'].isin(regions_of_interest)]

# Pivotear los datos para que cada fila represente un año y cada columna represente una región
pivoted_data = filtered_data.pivot(index='Year', columns='Country Name', values='Value')

# Eliminar filas que tengan valores NaN para asegurar una comparación justa
pivoted_data.dropna(inplace=True)

# Calcular la regresión lineal y el coeficiente de determinación R^2
slope, intercept, r_value, p_value, std_err = linregress(pivoted_data['Latin America & Caribbean'], pivoted_data['Europe & Central Asia'])
r_squared = r_value ** 2

# Crear el scatterplot
plt.figure(figsize=(10, 8))
sns.scatterplot(x=pivoted_data['Latin America & Caribbean'], y=pivoted_data['Europe & Central Asia'], label=f'Scatterplot')
sns.regplot(x=pivoted_data['Latin America & Caribbean'], y=pivoted_data['Europe & Central Asia'], scatter=False, color='red', label=f'Regresión Lineal (R^2 = {r_squared:.2f})')
plt.title('Comparación de la Densidad de Servidores entre Latin America & Caribbean y Europe & Central Asia')
plt.xlabel('Densidad de Servidores en Latin America & Caribbean')
plt.ylabel('Densidad de Servidores en Europe & Central Asia')
plt.legend()

plt.show()