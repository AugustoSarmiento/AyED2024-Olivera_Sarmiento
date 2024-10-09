from datetime import datetime

# Clase para representar el nodo del árbol AVL
class NodoAVL:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha  # Clave: la fecha
        self.temperatura = temperatura  # Valor: la temperatura
        self.izq = None  # Hijo izquierdo
        self.der = None  # Hijo derecho
        self.altura = 1  # Altura del nodo

# Clase para manejar el árbol AVL
class Temperaturas_DB:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._obtener_altura(y.izq), self._obtener_altura(y.der))
        x.altura = 1 + max(self._obtener_altura(x.izq), self._obtener_altura(x.der))
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._obtener_altura(x.izq), self._obtener_altura(x.der))
        y.altura = 1 + max(self._obtener_altura(y.izq), self._obtener_altura(y.der))
        return y

    def _obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izq) - self._obtener_altura(nodo.der)

    def _insertar(self, nodo, fecha, temperatura):
        if not nodo:
            return NodoAVL(fecha, temperatura)
        if fecha < nodo.fecha:
            nodo.izq = self._insertar(nodo.izq, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.der = self._insertar(nodo.der, fecha, temperatura)
        else:
            nodo.temperatura = temperatura
            return nodo

        nodo.altura = 1 + max(self._obtener_altura(nodo.izq), self._obtener_altura(nodo.der))
        balance = self._obtener_balance(nodo)

        if balance > 1 and fecha < nodo.izq.fecha:
            return self._rotar_derecha(nodo)
        if balance < -1 and fecha > nodo.der.fecha:
            return self._rotar_izquierda(nodo)
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        return nodo

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def _buscar(self, nodo, fecha):
        if not nodo:
            return None
        if fecha == nodo.fecha:
            return nodo.temperatura
        elif fecha < nodo.fecha:
            return self._buscar(nodo.izq, fecha)
        else:
            return self._buscar(nodo.der, fecha)

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        return self._buscar(self.raiz, fecha)

    def _rango_temperaturas(self, nodo, fecha1, fecha2, resultado):
        if not nodo:
            return
        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append(nodo.temperatura)
        if nodo.fecha > fecha1:
            self._rango_temperaturas(nodo.izq, fecha1, fecha2, resultado)
        if nodo.fecha < fecha2:
            self._rango_temperaturas(nodo.der, fecha1, fecha2, resultado)

    def max_temp_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        temperaturas = []
        self._rango_temperaturas(self.raiz, fecha1, fecha2, temperaturas)
        return max(temperaturas) if temperaturas else None

    def min_temp_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        temperaturas = []
        self._rango_temperaturas(self.raiz, fecha1, fecha2, temperaturas)
        return min(temperaturas) if temperaturas else None

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        temperaturas = []
        self._rango_temperaturas(self.raiz, fecha1, fecha2, temperaturas)
        if temperaturas:
            return min(temperaturas), max(temperaturas)
        return None, None

    def _borrar(self, nodo, fecha):
        if not nodo:
            return nodo
        if fecha < nodo.fecha:
            nodo.izq = self._borrar(nodo.izq, fecha)
        elif fecha > nodo.fecha:
            nodo.der = self._borrar(nodo.der, fecha)
        else:
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq
            temp = self._min_valor_nodo(nodo.der)
            nodo.fecha, nodo.temperatura = temp.fecha, temp.temperatura
            nodo.der = self._borrar(nodo.der, temp.fecha)
        nodo.altura = 1 + max(self._obtener_altura(nodo.izq), self._obtener_altura(nodo.der))
        balance = self._obtener_balance(nodo)
        if balance > 1 and self._obtener_balance(nodo.izq) >= 0:
            return self._rotar_derecha(nodo)
        if balance < -1 and self._obtener_balance(nodo.der) <= 0:
            return self._rotar_izquierda(nodo)
        if balance > 1 and self._obtener_balance(nodo.izq) < 0:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._obtener_balance(nodo.der) > 0:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        return nodo

    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self._borrar(self.raiz, fecha)

    def _rango_fechas(self, nodo, fecha1, fecha2, resultado):
        if not nodo:
            return
        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append(f"{nodo.fecha.strftime('%d/%m/%Y')}: {nodo.temperatura} ºC")
        if nodo.fecha > fecha1:
            self._rango_fechas(nodo.izq, fecha1, fecha2, resultado)
        if nodo.fecha < fecha2:
            self._rango_fechas(nodo.der, fecha1, fecha2, resultado)

    def devolver_temperaturas(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultado = []
        self._rango_fechas(self.raiz, fecha1, fecha2, resultado)
        return resultado

    def _contar_nodos(self, nodo):
        if not nodo:
            return 0
        return 1 + self._contar_nodos(nodo.izq) + self._contar_nodos(nodo.der)

    def cantidad_muestras(self):
        return self._contar_nodos(self.raiz)
