from modules.Temperaturas_DB import Temperaturas_DB
from modules.Temperaturas_DB import generar_fechas_aleatorias
import random


from datetime import datetime
# Crear la base de datos de temperaturas
temperaturas_db = Temperaturas_DB()

# Rango de fechas para las mediciones
start_date = datetime.strptime("01/01/2020", "%d/%m/%Y")
end_date = datetime.strptime("31/12/2020", "%d/%m/%Y")

    # Generar 100 fechas aleatorias
fechas_aleatorias = generar_fechas_aleatorias(100, start_date, end_date)

    # Generar temperaturas aleatorias y guardarlas en la base de datos
for fecha in fechas_aleatorias:
    temperatura = round(random.uniform(-30, 50), 2)  # Temperatura entre -30 y 50 ºC
    temperaturas_db.guardar_temperatura(temperatura, fecha)

    # Ejemplo de uso de la base de datos
print("Cantidad de muestras:", temperaturas_db.cantidad_muestras())
print("Temperaturas en el rango 01/01/2020 a 31/12/2020:")
print(temperaturas_db.devolver_temperaturas("01/01/2020", "31/12/2020"))
print("Temperatura en 15/07/2020:", temperaturas_db.devolver_temperatura("15/07/2020"))
print("Temperatura máxima entre 01/06/2020 y 30/06/2020:", temperaturas_db.max_temp_rango("01/06/2020", "30/06/2020"))
print("Temperatura mínima entre 01/06/2020 y 30/06/2020:", temperaturas_db.min_temp_rango("01/06/2020", "30/06/2020"))
print("Temperaturas mínimas y máximas entre 01/06/2020 y 30/06/2020:", temperaturas_db.temp_extremos_rango("01/06/2020", "30/06/2020"))

