from datetime import datetime
from modules.Arbol_AVL import AVLTree

class Temperaturas_DB:
    def __init__(self):
        self.__arbol = AVLTree()  # Objeto AVLTree para gestionar las operaciones AVL
        self.__raiz = None  # Nodo raíz del árbol AVL
        self.__muestras = 0  # Contador de muestras en la base de datos

    # Property para acceder al árbol AVL
    @property
    def arbol(self):
        return self.__arbol

    # Property para la raíz del árbol
    @property
    def raiz(self):
        return self.__raiz
    
    @raiz.setter
    def raiz(self, valor):
        self.__raiz = valor

    # Property para el contador de muestras
    @property
    def muestras(self):
        return self.__muestras
    
    @muestras.setter
    def muestras(self, valor):
        if valor < 0:
            raise ValueError("La cantidad de muestras no puede ser negativa.")
        self.__muestras = valor

    # Método para guardar temperatura en el AVL y aumentar la cantidad de muestras
    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self.arbol.insertar(self.raiz, fecha, temperatura)
        self.muestras += 1

    # Método para devolver la temperatura de una fecha específica
    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        return self.arbol.buscar(self.raiz, fecha)

    # Método para obtener la temperatura máxima en un rango de fechas
    def max_temp_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return max(resultados, key=lambda x: x[1])[1] if resultados else None

    # Método para obtener la temperatura mínima en un rango de fechas
    def min_temp_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return min(resultados, key=lambda x: x[1])[1] if resultados else None

    # Método para obtener la temperatura mínima y máxima en un rango de fechas
    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return (min(resultados, key=lambda x: x[1])[1], max(resultados, key=lambda x: x[1])[1]) if resultados else (None, None)

    # Método para borrar una temperatura dada una fecha
    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self.arbol.eliminar(self.raiz, fecha)
        self.muestras -= 1

    # Método para devolver una lista de temperaturas en un rango de fechas
    def devolver_temperaturas(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in resultados]

    # Método para obtener la cantidad de muestras
    def cantidad_muestras(self):
        return self.muestras
