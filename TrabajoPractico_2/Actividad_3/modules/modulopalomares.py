class Aldea:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__vecinos = {}  # Diccionario de aldeas vecinas y sus distancias
        self.__predecesor = None  # Aldea desde la que se recibe la noticia
        self.__replica_a = []  # Aldeas a las que se enviarán réplicas
    
    # Getters y setters
    def get_nombre(self):
        return self.__nombre

    def get_predecesor(self):
        return self.__predecesor

    def set_predecesor(self, predecesor):
        self.__predecesor = predecesor

    def get_vecinos(self):
        return self.__vecinos

    def agregar_vecino(self, vecino, distancia):
        self.__vecinos[vecino] = distancia

    def agregar_replica(self, vecino):
        self.__replica_a.append(vecino)

    def get_replica_a(self):
        return self.__replica_a


class SistemaDePalomas:
    def __init__(self, archivo):
        self.__aldeas = {}
        self.cargar_aldeas(archivo)
    
    def cargar_aldeas(self, archivo):
    # Cargar las aldeas y sus conexiones desde un archivo de texto
        with open(archivo, 'r') as f:
            for linea in f:
                # Ignorar líneas vacías o líneas mal formateadas
                partes = linea.strip().split(',')
                
                # Verificar que la línea tenga exactamente 3 elementos
                if len(partes) != 3:
                    continue  # Saltar esta línea si no tiene el formato esperado
                
                aldea1, aldea2, distancia = partes
                distancia = int(distancia)

                if aldea1 not in self.__aldeas:
                    self.__aldeas[aldea1] = Aldea(aldea1)
                if aldea2 not in self.__aldeas:
                    self.__aldeas[aldea2] = Aldea(aldea2)

                self.__aldeas[aldea1].agregar_vecino(self.__aldeas[aldea2], distancia)
                self.__aldeas[aldea2].agregar_vecino(self.__aldeas[aldea1], distancia)


    def prim(self, inicio):
        # Inicialización del algoritmo de Prim
        no_visitados = set(self.__aldeas.values())  # Conjunto de aldeas no visitadas
        visitados = set()  # Conjunto de aldeas visitadas
        aristas_mst = []  # Lista de las aristas en el Árbol de Expansión Mínimo
        total_distancia = 0
        
        # Comenzamos desde la aldea de inicio (Peligros)
        visitados.add(inicio)

        # Bucle principal de Prim
        while len(visitados) < len(self.__aldeas):
            # Encontrar la arista más corta que conecte una aldea visitada con una no visitada
            aldea_actual = None
            vecino_min = None
            distancia_min = float('inf')
            
            for aldea in visitados:
                for vecino, distancia in aldea.get_vecinos().items():
                    if vecino not in visitados and distancia < distancia_min:
                        aldea_actual = aldea
                        vecino_min = vecino
                        distancia_min = distancia
            
            if vecino_min:
                # Marcar el vecino como visitado
                visitados.add(vecino_min)
                aristas_mst.append((aldea_actual, vecino_min, distancia_min))
                total_distancia += distancia_min

                # Configurar el predecesor para el envío de réplicas
                vecino_min.set_predecesor(aldea_actual)
                aldea_actual.agregar_replica(vecino_min)

        return total_distancia

    def mostrar_resultados(self):
        # Imprimir la lista de aldeas en orden alfabético
        aldeas_ordenadas = sorted(self.__aldeas.values(), key=lambda x: x.get_nombre())
        for aldea in aldeas_ordenadas:
            print(f'Aldea: {aldea.get_nombre()}')
            if aldea.get_predecesor():
                print(f'  Recibe noticias de: {aldea.get_predecesor().get_nombre()}')
            if aldea.get_replica_a():
                replicas = [a.get_nombre() for a in aldea.get_replica_a()]
                print(f'  Envía réplicas a: {", ".join(replicas)}')
            else:
                print(f'  No envía réplicas')

    def suma_distancias(self):
        # Calcular la suma de todas las distancias recorridas en el MST
        suma = 0
        for aldea in self.__aldeas.values():
            if aldea.get_predecesor():
                suma += aldea.get_vecinos()[aldea.get_predecesor()]
        return suma


# Implementación en main
def main():
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


if __name__ == '__main__':
    main()
