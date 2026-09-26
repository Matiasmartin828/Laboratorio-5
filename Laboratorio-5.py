# LABORATORIO 5
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-5.git

import numpy as np                                                                              #Librerías
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

dataframe['alerta'] = alerta                                                                    #Creo una nueva columna en el DataFrame llamada 'alerta'
fig, ax = plt.subplots(figsize=(10, 5))                                                         #Creo una figura y un eje para graficar, con un tamaño de 10x5 pulgadas
ax.plot(dataframe.index, dataframe['temperatura_C'], label='Temperatura (°C)', color='red')     #Grafico la columna 'temperatura_C' en el eje y, con el índice del DataFrame en el eje x, y le asigno una etiqueta y un color
ax.plot(dataframe.index, dataframe['voltaje_bateria_V'], label='Voltaje (V)', color='blue')     #Grafico la columna 'voltaje_bateria_V' en el eje y, con el índice del DataFrame en el eje x, y le asigno una etiqueta y un color
alertas_tiempo = dataframe.index[alerta]                                                        #Extraigo los valores del índice del DataFrame donde se cumplen las condiciones de alerta
alertas_voltaje = dataframe['voltaje_bateria_V'][alerta] 
ax.scatter(alertas_tiempo, alertas_voltaje, color='red', marker='x', label='Alerta', zorder=5)  #Agrego las marcas de las alertas en el gráfico añadiendo un gráfico de dispersión
ax.set_title('Evolución temporal de telemetría', fontsize=16)                                                                 #Agrego un título al gráfico con un tamaño de fuente de 14
ax.legend()                                                                                    
ax.set_xlabel('Tiempo', fontsize=11)                                                            #Agrego una etiqueta al eje x con un tamaño de fuente de 12
ax.set_ylabel('Magnitud', fontsize=11)
plt.tight_layout()
plt.show()
resumen_diario = dataframe.resample('D').agg(temperatura_promedio=('temperatura_C', 'mean'),    #Creo el resumen diario de los datos, agrupando por día y calculando la temperatura promedio, máxima y mínima, el voltaje promedio y mínimo, y la cantidad de alertas
        temperatura_maxima=('temperatura_C', 'max'),
        temperatura_minima=('temperatura_C', 'min'),
        voltaje_promedio=('voltaje_bateria_V', 'mean'),
        voltaje_minimo=('voltaje_bateria_V', 'min'), 
        cantidad_alertas=('alerta', 'sum')).round(2)                                            #Redondeo los valores del resumen diario a dos decimales
print("\nResumen Diario:")
print(resumen_diario)
resumen_diario.to_excel('Resumen diario.xlsx', sheet_name='Resumen diario')                     #Exporto el DataFrame a un archivo excel
print('\nEl archivo "Resumen diario" se ha generado correctamente.') 
