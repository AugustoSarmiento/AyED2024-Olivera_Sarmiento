from modules.ClasesInteres import ArbolMST
from modules.ColaPrioridad import ColaPrioridad

def prim(grafo, inicio_id):
    cp = ColaPrioridad()

    for vertice in grafo:
        vertice.asignar_distancia(float('inf'))
        vertice.asignar_predecesor(None)

    inicio = grafo.obtener_vertice(inicio_id)
    inicio.asignar_distancia(0)
    cp.construir_monticulo([(vertice.obtener_distancia(), vertice) for vertice in grafo])
    
    visitados = set() 

    while not cp.esta_vacia():

        distancia_actual, vertice_actual = cp.eliminar_min()

        if vertice_actual in visitados:
            continue
        
        visitados.add(vertice_actual)
        print(f"Seleccionado: {vertice_actual.obtener_id()} con distancia {distancia_actual}")

        for vecino in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vecino)
            

            if vecino not in visitados and nuevo_costo < vecino.obtener_distancia():
                vecino.asignar_predecesor(vertice_actual)
                vecino.asignar_distancia(nuevo_costo)
                
                cp.decrementar_clave(vecino, nuevo_costo)
                print(f"Actualizado: {vecino.obtener_id()} con nuevo costo {nuevo_costo}")


    arbol_mst = ArbolMST()
    for vertice in grafo:
        predecesor = vertice.obtener_predecesor()
        if predecesor:
            distancia = vertice.obtener_distancia()
            arbol_mst.agregar_conexion(predecesor.obtener_id(), vertice.obtener_id(), distancia)

    print(f"Suma total del MST generado: {arbol_mst.total_distancia}")
    
    return arbol_mst