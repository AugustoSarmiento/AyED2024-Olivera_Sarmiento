from modules.modulopalomares import Aldea
from modules.modulopalomares import SistemaDePalomas
# Instanciar el sistema de palomas con un archivo que contiene las aldeas y sus distancias
archivo = 'C:\AyED2024-Olivera_Sarmiento\TrabajoPractico_2\Actividad_3\docs\aldeas.txt'  # Este archivo debe contener las conexiones de las aldeas
sistema = SistemaDePalomas(archivo)
    
# Aldea Peligros es la de inicio
aldea_inicio = sistema.aldeas['Peligros']
    
# Ejecutar el algoritmo de Dijkstra para encontrar los caminos más cortos
sistema.dijkstra(aldea_inicio)
    
# Mostrar los resultados
sistema.mostrar_resultados()
    
# Mostrar la suma de todas las distancias recorridas por las palomas
suma_distancias = sistema.suma_distancias()
print(f'Suma total de distancias recorridas por las palomas: {suma_distancias} leguas')
