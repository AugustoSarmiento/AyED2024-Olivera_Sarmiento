from modules.ClasesInteres import ArbolMST
from modules.ColaPrioridad import ColaPrioridad

def prim(grafo, inicio_id):
    cp = ColaPrioridad()

    # Inicializar todos los vértices con distancia infinita y sin predecesor
    for vertice in grafo:
        vertice.asignar_distancia(float('inf'))
        vertice.asignar_predecesor(None)

    # Configurar el vértice de inicio con distancia 0
    inicio = grafo.obtener_vertice(inicio_id)
    inicio.asignar_distancia(0)
    cp.construir_monticulo([(vertice.obtener_distancia(), vertice) for vertice in grafo])
    
    visitados = set()

    # Algoritmo de Prim
    while not cp.esta_vacia():
        distancia_actual, vertice_actual = cp.eliminar_min()

        if vertice_actual in visitados:
            continue
        
        visitados.add(vertice_actual)

        # Verificar conexiones de cada vecino
        for vecino in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vecino)
            
            # Si el vecino no ha sido visitado y encontramos un camino más corto
            if vecino not in visitados and nuevo_costo < vecino.obtener_distancia():
                vecino.asignar_predecesor(vertice_actual)
                vecino.asignar_distancia(nuevo_costo)
                
                # Actualizar la cola de prioridad
                cp.decrementar_clave(vecino, nuevo_costo)

    # Construir el MST resultante
    arbol_mst = ArbolMST()
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor:
            distancia = vertice.obtener_distancia()
            arbol_mst.agregar_conexion(predecesor.obtener_id(), vertice.obtener_id(), distancia)
    
    return arbol_mst
