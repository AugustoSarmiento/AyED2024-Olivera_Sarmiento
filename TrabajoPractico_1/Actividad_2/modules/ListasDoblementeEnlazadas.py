#consigna 2
class Nodo:
    def __init__(self, data):
        self.data = data
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola =None
        self.tamanio =0

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola =nuevo_nodo

        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo  
        self.tamanio += 1
    
    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamanio+=1
            
    def esta_vacia(self): 
        if self.cabeza == None:
            return (print(True))
        else:
            return (print(False))
               
    def __len__(self):
        cant_elementos = self.tamanio
        return
    
    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
            
        if posicion < 0 or posicion > self.tamanio:
            raise ValueError("La posición dada no está incluída en la lista.")

        if posicion == 0:
            self.agregar_al_principio(item)

        if posicion == self.tamanio:
            self.agregar_al_final(item)

        nuevo_nodo = Nodo(item)
        actual = self.cabeza
        for i in range(posicion - 1):
            actual = actual.siguiente

        nuevo_nodo.anterior = actual
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo

        self.tamanio += 1

    def extraer (self, posicion = None):
        if self.tamanio == 0:
            raise IndexError("La lista está vacía")

        if posicion is None:
            item = self.cola.data
            if self.tamanio == 1:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
        else:
            if posicion < 0 or posicion >= self.tamanio:
                raise IndexError("La posición dada no forma parte de la lista")
            
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente

            item = actual.data
            if actual == self.cabeza:
                self.cabeza = actual.siguiente
            else:
                actual.anterior.siguiente = actual.siguiente
            if actual == self.cola:
                self.cola = actual.anterior
            else:
                actual.siguiente.anterior = actual.anterior

        self.tamanio -= 1
        return item    
    
    def copiar(self):
        nueva_lista = ListaDoblementeEnlazada()
        actual = self.cabeza

        while actual:
            nuevo_nodo = Nodo(actual.data)
            if nueva_lista.cabeza is None:
                nueva_lista.cabeza = nuevo_nodo
                nueva_lista.cola = nuevo_nodo
            else:
                nueva_lista.cola.siguiente = nuevo_nodo
                nuevo_nodo.anterior = nueva_lista.cola
                nueva_lista.cola = nuevo_nodo
            actual = actual.siguiente

        return nueva_lista

    def invertir(self):
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = actual.anterior
            actual.anterior = siguiente
            actual = siguiente
        self.cabeza, self.cola = self.cola, self.cabeza
        return self

    def concatenar(self, otra_lista):
        if self.cola is None:
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
        else:
            self.cola.siguiente = otra_lista.cabeza
            otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola

        return self
    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista