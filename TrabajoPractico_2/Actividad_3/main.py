from modules.AlgoritmoPrim import prim
from modules.FuncionesGrafo import cargar_grafo_desde_archivo, mostrar_resultados

archivo = "C:/AyED2024-Olivera_Sarmiento/TrabajoPractico_2/Actividad_3/docs/aldeas.txt"
grafo = cargar_grafo_desde_archivo(archivo)
arbol_mst = prim(grafo, "Peligros")

# Aquí se pasa arbol_mst en lugar de grafo
mostrar_resultados(arbol_mst)
