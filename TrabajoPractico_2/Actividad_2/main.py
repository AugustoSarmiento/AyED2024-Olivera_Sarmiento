import random
from datetime import datetime, timedelta
from modules.Temperaturas_DB import Temperaturas_DB

# Crear una instancia de la base de datos de temperaturas
db = Temperaturas_DB()

# Generar 100 muestras aleatorias
for _ in range(100):
    # Generar una fecha aleatoria en los últimos 100 días
    fecha = datetime.now() - timedelta(days=random.randint(0, 100))
    fecha_str = fecha.strftime("%d/%m/%Y")
    
    # Generar una temperatura aleatoria entre -30°C y 50°C
    temperatura = round(random.uniform(-30, 50), 2)
    
    # Intentar guardar la muestra en la base de datos
    try:
        db.guardar_temperatura(temperatura, fecha_str)
    except ValueError as e:
        print(f"Advertencia: {e}")  # Opcional: imprimir advertencia si la fecha ya existe
        continue  # Continuar con la siguiente muestra en caso de fecha duplicada

# Ejemplo de pruebas
print("Cantidad de muestras:", db.cantidad_muestras())
print("Temperatura en una fecha específica:", db.devolver_temperatura("01/10/2024"))

# Ejemplo de rango de fechas
fecha_inicio = "01/01/2023"
fecha_fin = datetime.now().strftime("%d/%m/%Y")

print("Temperatura máxima en rango:", db.max_temp_rango(fecha_inicio, fecha_fin))
print("Temperatura mínima en rango:", db.min_temp_rango(fecha_inicio, fecha_fin))
print("Temperaturas en el rango:")
for temp in db.devolver_temperaturas(fecha_inicio, fecha_fin):
    print(temp)
