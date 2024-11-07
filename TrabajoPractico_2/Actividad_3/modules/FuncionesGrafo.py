from modules.Grafo import Grafo

def mostrar_resultados(grafo):
    nombres_aldeas = sorted(grafo.obtener_vertices())
    print("Lista de Aldeas en orden alfabético:")
    for nombre in nombres_aldeas:
        print(nombre)

    print("\nRutas de envío de noticias:")
    total_distancia = 0
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor:
            distancia = vertice.obtener_distancia()
            total_distancia += distancia
            print(f"Desde {predecesor.obtener_id()} se envía a {vertice.obtener_id()} con distancia {distancia} leguas.")

    print(f"\nSuma total de distancias recorridas: {total_distancia} leguas.")


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