from modules.Grafo import Grafo

from modules.AlgoritmoPrim import prim

def mostrar_resultados(arbol_mst):
    print("\nRutas de envío de noticias:")
    
    total_distancia = 0
    for origen, destino, distancia in arbol_mst.conexiones:
        total_distancia += distancia
        print(f"Desde {origen} se envía a {destino} con distancia {distancia} leguas.")

    print(f"\nSuma total de distancias recorridas en el MST: {total_distancia} leguas.")



def cargar_grafo_desde_archivo(nombre_archivo):
    grafo = Grafo()
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if len(datos) == 3:
                nodo1, nodo2, peso = datos[0].strip(), datos[1].strip(), int(datos[2].strip())
                grafo.agregar_arista(nodo1, nodo2, peso)
            elif len(datos) == 1 and datos[0].strip():
                grafo.agregar_vertice(datos[0].strip())
    return grafo