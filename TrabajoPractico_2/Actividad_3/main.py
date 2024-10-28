from modules.modulopalomares import SistemaDePalomas

# Instanciar el sistema de palomas con un archivo que contiene las aldeas y sus distancias
archivo = 'docs/aldeas.txt'  # Este archivo debe contener las conexiones de las aldeas
sistema = SistemaDePalomas(archivo) 
# Aldea Peligros es la de inicio
aldea_inicio = sistema._SistemaDePalomas__aldeas['Peligros']
    
# Ejecutar el algoritmo de Prim para encontrar el Árbol de Expansión Mínimo
total_distancia = sistema.prim(aldea_inicio)
    
# Mostrar los resultados
sistema.mostrar_resultados()
    
# Mostrar la suma total de distancias recorridas
print(f'Suma total de distancias recorridas por las palomas: {total_distancia} leguas')
