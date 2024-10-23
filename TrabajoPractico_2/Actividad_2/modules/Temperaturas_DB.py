from datetime import datetime

class Temperaturas_DB:
    class _NodoAVL:
        """Clase privada para representar cada nodo del árbol AVL."""
        def __init__(self, fecha, temperatura):
            self.fecha = fecha  # Objeto datetime
            self.temperatura = temperatura
            self.izq = None
            self.der = None
            self.altura = 1  # Almacenamos la altura del nodo para balanceo

    def __init__(self):
        """Inicializa el árbol AVL vacío."""
        self._raiz = None

    def _obtener_altura(self, nodo):
        """Devuelve la altura de un nodo, o 0 si el nodo es None."""
        if not nodo:
            return 0
        return nodo.altura

    def _actualizar_altura(self, nodo):
        """Actualiza la altura de un nodo basado en sus hijos."""
        nodo.altura = 1 + max(self._obtener_altura(nodo.izq), self._obtener_altura(nodo.der))

    def _obtener_balance(self, nodo):
        """Devuelve el factor de balance de un nodo."""
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izq) - self._obtener_altura(nodo.der)

    def _rotar_derecha(self, y):
        """Realiza una rotación a la derecha."""
        x = y.izq
        T2 = x.der
        # Rotar
        x.der = y
        y.izq = T2
        # Actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x

    def _rotar_izquierda(self, x):
        """Realiza una rotación a la izquierda."""
        y = x.der
        T2 = y.izq
        # Rotar
        y.izq = x
        x.der = T2
        # Actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y

    def _insertar(self, nodo, fecha, temperatura):
        """Inserta un nuevo nodo en el árbol AVL."""
        if not nodo:
            return self._NodoAVL(fecha, temperatura)

        if fecha < nodo.fecha:
            nodo.izq = self._insertar(nodo.izq, fecha, temperatura)
        elif fecha > nodo.fecha:
            nodo.der = self._insertar(nodo.der, fecha, temperatura)
        else:
            raise ValueError("Ya existe una medición con esa fecha")

        # Actualizar altura del nodo padre
        self._actualizar_altura(nodo)

        # Balancear el nodo
        balance = self._obtener_balance(nodo)

        # Caso 1: Rotación derecha si está desbalanceado hacia la izquierda
        if balance > 1 and fecha < nodo.izq.fecha:
            return self._rotar_derecha(nodo)

        # Caso 2: Rotación izquierda si está desbalanceado hacia la derecha
        if balance < -1 and fecha > nodo.der.fecha:
            return self._rotar_izquierda(nodo)

        # Caso 3: Rotación izquierda-derecha
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)

        # Caso 4: Rotación derecha-izquierda
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    def guardar_temperatura(self, temperatura, fecha_str):
        """Guarda una nueva temperatura asociada a una fecha."""
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self._raiz = self._insertar(self._raiz, fecha, temperatura)


