from datetime import datetime
from modules.Arbol_AVL import AVLTree

class Temperaturas_DB:
    def __init__(self):
        self.arbol = AVLTree()
        self.root = None

    def guardar_temperatura(self, temperatura, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.root = self.arbol.insertar(self.root, fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        return self.arbol.buscar(self.root, fecha_dt)

    def max_temp_rango(self, fecha1, fecha2):
        temperaturas = self._obtener_rango_temperaturas(fecha1, fecha2)
        return max(temp[1] for temp in temperaturas) if temperaturas else None

    def min_temp_rango(self, fecha1, fecha2):
        temperaturas = self._obtener_rango_temperaturas(fecha1, fecha2)
        return min(temp[1] for temp in temperaturas) if temperaturas else None

    def temp_extremos_rango(self, fecha1, fecha2):
        temperaturas = self._obtener_rango_temperaturas(fecha1, fecha2)
        if temperaturas:
            min_temp = min(temp[1] for temp in temperaturas)
            max_temp = max(temp[1] for temp in temperaturas)
            return min_temp, max_temp
        return None, None

    def borrar_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.root = self.arbol.eliminar(self.root, fecha_dt)

    def devolver_temperaturas(self, fecha1, fecha2):
        temperaturas = self._obtener_rango_temperaturas(fecha1, fecha2)
        return [f"{temp[0].strftime('%d/%m/%Y')}: {temp[1]} ºC" for temp in temperaturas]

    def cantidad_muestras(self):
        return self.arbol.contar_nodos(self.root)

    # Método auxiliar para obtener temperaturas en un rango
    def _obtener_rango_temperaturas(self, fecha1, fecha2):
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.root, fecha1_dt, fecha2_dt, resultados)
        return resultados
