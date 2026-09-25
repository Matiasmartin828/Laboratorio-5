# LABORATORIO 5
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-5.git

import tkinter as tk                                                                            #Librería para crear interfaces gráficas de usuario (GUI)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv('telemetria_nodo_iot.csv', parse_dates=['timestamp'])                   #Leo el archivo CSV y convierto la columna 'timestamp' a tipo datetime
dataframe = dataframe.set_index('timestamp')                                                    #Establezco la columna 'timestamp' como índice
print("Estadísticas descriptivas:\n")
estadisticas = dataframe.describe().loc[['mean', 'min', 'max', 'std']]                          #Muestro las estadísticas descriptivas de las columnas numéricas del DataFrame, incluyendo la media, el valor mínimo, el valor máximo y la desviación estándar
print(estadisticas, "\n")

                                  