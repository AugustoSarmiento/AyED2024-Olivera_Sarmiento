class Aldea:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__vecinas = []
        self.__predecesor = None

    def agregar_vecina(self, vecina, distancia):
        self.__vecinas.append((distancia, vecina))

    def obtener_nombre(self):
        return self.__nombre

    def obtener_vecinas(self):
        return self.__vecinas

    def establecer_predecesor(self, predecesor):
        self.__predecesor = predecesor

    def obtener_predecesor(self):
        return self.__predecesor

    def __lt__(self, other):
        return self.__nombre < other.obtener_nombre()
    
class ArbolMST:
    def __init__(self):
        self.conexiones = [] 
        self.total_distancia = 0 

    def agregar_conexion(self, origen, destino, distancia):
        self.conexiones.append((origen, destino, distancia))
        self.total_distancia += distancia

    def mostrar_arbol(self):
        print("Rutas del MST:")
        for origen, destino, distancia in self.conexiones:
            print(f"{origen} - {destino} : {distancia}")
        print(f"Distancia total del MST: {self.total_distancia}")