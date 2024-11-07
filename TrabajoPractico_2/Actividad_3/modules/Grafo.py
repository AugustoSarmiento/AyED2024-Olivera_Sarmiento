class Vertice:
    def __init__(self, clave):
        self.__id = clave
        self.__conectadoA = {}
        self.__distancia = float('inf')
        self.__predecesor = None

    def agregar_vecino(self, vecino, ponderacion=0):
        self.__conectadoA[vecino] = ponderacion

    def obtener_id(self):
        return self.__id

    def obtener_conexiones(self):
        return self.__conectadoA.keys()

    def obtener_ponderacion(self, vecino):
        return self.__conectadoA[vecino]

    def asignar_distancia(self, distancia):
        self.__distancia = distancia

    def obtener_distancia(self):
        return self.__distancia


    def asignar_predecesor(self, predecesor):
        self.__predecesor = predecesor

    def obtener_predecesor(self):
        return self.__predecesor

    def __lt__(self, other):
        return self.__distancia < other.obtener_distancia()

class Grafo:
    def __init__(self):
        self.__listaVertices = {}
        self.__numVertices = 0

    def agregar_vertice(self, clave):
        nuevoVertice = Vertice(clave)
        self.__listaVertices[clave] = nuevoVertice
        self.__numVertices += 1
        return nuevoVertice

    def obtener_vertice(self, clave):
        return self.__listaVertices.get(clave, None)

    def agregar_arista(self, de, a, costo=0):
        if de not in self.__listaVertices:
            self.agregar_vertice(de)
        if a not in self.__listaVertices:
            self.agregar_vertice(a)
        self.__listaVertices[de].agregar_vecino(self.__listaVertices[a], costo)
        self.__listaVertices[a].agregar_vecino(self.__listaVertices[de], costo)  

    def obtener_vertices(self):
        return self.__listaVertices.keys()

    def __iter__(self):
        return iter(self.__listaVertices.values())