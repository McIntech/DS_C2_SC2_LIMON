""" PROYECTO DS_C2_SC2_FRANCO """
import numpy as np
import pandas as pd


# A. Extraer la información del archivo.
df = pd.read_csv("./country_vaccinations.csv")
print("Our dataframe \n", df)

# B. Mostrar la estructura y tipos de datos de cada columna, asegurándote que las columnas con fechas sean del tipo datetime64.

df.info()

# c. Determinar la cantidad de vacunas aplicadas de cada compañía (con base en cómo lo reporta cada país en la columna vaccines, en otras palabras, agrupe por vaccines y realice la sumatoria).
df.columns = df.columns.str.strip()
df_grouped = df.groupby("vaccines").sum(numeric_only=True)
print(df_grouped.head())

# d. Obtener la cantidad de vacunas aplicadas en todo el mundo.

# e. Calcular el promedio de vacunas aplicadas por país.

# f. Determinar la cantidad de vacunas aplicadas el día 29/01/21 en todo el mundo.

# g. Crear un dataframe nuevo denominado conDiferencias que contenga los datos originales y una columna derivada (diferencias) con las diferencias de aplicación entre las columnas daily_vaccionations y daily_vaccionations_raw.

# h. Obtener el periodo de tiempo entre el registro con fecha más reciente y el registro con fecha más antigua.
