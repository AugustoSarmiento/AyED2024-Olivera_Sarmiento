class NodoAVL:
    def __init__(self, fecha, valor):
        self.fecha = fecha
        self.valor = valor
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class AVLTree:
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance_factor(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)) + 1
        x.altura = max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)) + 1
        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = max(self.obtener_altura(x.izquierda), self.obtener_altura(x.derecha)) + 1
        y.altura = max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha)) + 1
        return y

    def insertar(self, nodo, fecha, valor):
        if not nodo:
            return NodoAVL(fecha, valor)

        if fecha < nodo.fecha:
            nodo.izquierda = self.insertar(nodo.izquierda, fecha, valor)
        else:
            nodo.derecha = self.insertar(nodo.derecha, fecha, valor)

        nodo.altura = max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha)) + 1

        balance = self.balance_factor(nodo)

        if balance > 1 and fecha < nodo.izquierda.fecha:
            return self.rotacion_derecha(nodo)

        if balance < -1 and fecha > nodo.derecha.fecha:
            return self.rotacion_izquierda(nodo)

        if balance > 1 and fecha > nodo.izquierda.fecha:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        if balance < -1 and fecha < nodo.derecha.fecha:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def buscar(self, nodo, fecha):
        if not nodo:
            raise ValueError("Fecha no encontrada.")
        if fecha == nodo.fecha:
            return nodo.valor
        elif fecha < nodo.fecha:
            return self.buscar(nodo.izquierda, fecha)
        else:
            return self.buscar(nodo.derecha, fecha)

    def min_value_node(self, nodo):
        if nodo is None or nodo.izquierda is None:
            return nodo
        return self.min_value_node(nodo.izquierda)

    def eliminar(self, nodo, fecha):
        if not nodo:
            raise ValueError("Fecha no encontrada.")

        if fecha < nodo.fecha:
            nodo.izquierda = self.eliminar(nodo.izquierda, fecha)
        elif fecha > nodo.fecha:
            nodo.derecha = self.eliminar(nodo.derecha, fecha)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            temp = self.min_value_node(nodo.derecha)
            nodo.fecha = temp.fecha
            nodo.valor = temp.valor
            nodo.derecha = self.eliminar(nodo.derecha, temp.fecha)

        if nodo is None:
            return nodo

        nodo.altura = max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha)) + 1
        balance = self.balance_factor(nodo)

        if balance > 1 and self.balance_factor(nodo.izquierda) >= 0:
            return self.rotacion_derecha(nodo)

        if balance > 1 and self.balance_factor(nodo.izquierda) < 0:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        if balance < -1 and self.balance_factor(nodo.derecha) <= 0:
            return self.rotacion_izquierda(nodo)

        if balance < -1 and self.balance_factor(nodo.derecha) > 0:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    def inorden_rango(self, nodo, fecha1, fecha2, resultados):
        if not nodo:
            return
        if fecha1 <= nodo.fecha <= fecha2:
            self.inorden_rango(nodo.izquierda, fecha1, fecha2, resultados)
            resultados.append((nodo.fecha, nodo.valor))
            self.inorden_rango(nodo.derecha, fecha1, fecha2, resultados)
        elif nodo.fecha < fecha1:
            self.inorden_rango(nodo.derecha, fecha1, fecha2, resultados)
        else:
            self.inorden_rango(nodo.izquierda, fecha1, fecha2, resultados)