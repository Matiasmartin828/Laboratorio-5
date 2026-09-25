# LABORATORIO 5
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-5.git

import tkinter as tk                                                                            #Librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv('telemetria_nodo_iot.csv', parse_dates=['timestamp'])                   #Leo el archivo CSV y convierto la columna 'timestamp' a tipo datetime
dataframe = dataframe.set_index('timestamp')                                                    #Establezco la columna 'timestamp' como índice
print("Estadísticas descriptivas:\n")
estadisticas = dataframe.describe().loc[['mean', 'min', 'max', 'std']]                          #Muestro las estadísticas descriptivas de las columnas numéricas del DataFrame, incluyendo la media, el valor mínimo, el valor máximo y la desviación estándar
print(estadisticas, "\n")
voltajes = dataframe['voltaje_bateria_V'].to_numpy()                                            #Extraigo los valores de la columna 'voltaje_bateria_V' y los convierto a un arreglo de NumPy
potencias = dataframe['rssi_dbm'].to_numpy()                                                    #Extraigo los valores de la columna 'rssi_dbm' y los convierto a un arreglo de NumPy
alerta_bateria = voltajes < 3.5
alerta_señal = potencias < -85
alerta = alerta_bateria | alerta_señal                                                          #Defino la alerta general
alertas_bateria = len(dataframe[alerta_bateria])                                                #Chequeo cuantos registros cumplen las condiciones de las alertas
alertas_senal = len(dataframe[alerta_señal])
alertas_general = len(dataframe[alerta])
print("Conteo de alertas:")                                                                     #Muestro el conteo de alertas por cada condición y el total de registros con al menos una alerta
print("Batería baja (< 3.5 V): ", alertas_bateria)
print("Señal débil (< -85 dBm): ", alertas_senal)
print("Registros con al menos una alerta: ", alertas_general, "\n")

       
                                  