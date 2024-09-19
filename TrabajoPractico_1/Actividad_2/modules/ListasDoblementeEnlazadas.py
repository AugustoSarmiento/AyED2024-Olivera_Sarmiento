#consigna 2
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola =None
        self.tamanio =0
    
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente


    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola =nuevo_nodo
            self.tamanio += 1
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo  
            self.tamanio += 1
    
    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
            self.tamanio += 1
        else:
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            self.tamanio+=1

            
    def esta_vacia(self): 
        if self.cabeza == None:
            return True
        else:
            return False
               
    def __len__(self):
        cant_elementos = self.tamanio
        return cant_elementos
    
    def insertar(self, item, posicion=None):
        if posicion is None:
            self.agregar_al_final(item)
        elif posicion < 0 or posicion > self.tamanio:
            raise ValueError("La posición dada no está incluída en la lista.")
        else:
            nuevo_nodo = Nodo(item)
            if posicion == 0:
                nuevo_nodo.siguiente = self.cabeza
                if self.cabeza:
                    self.cabeza.anterior = nuevo_nodo
                self.cabeza = nuevo_nodo
            else:
                actual = self.cabeza
                for _ in range(posicion - 1):
                    actual = actual.siguiente
                nuevo_nodo.anterior = actual
                nuevo_nodo.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = nuevo_nodo
                actual.siguiente = nuevo_nodo

            self.tamanio += 1


    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise IndexError("Lista vacía")
        if posicion is None:
            posicion = self.tamanio - 1
        if posicion < 0:
            posicion += self.tamanio
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            valor = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            valor = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            valor = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return valor    
    
    def copiar(self):
        nueva_lista = ListaDoblementeEnlazada()
        actual = self.cabeza
        while actual:
            nuevo_nodo = Nodo(actual.dato)  # Crea un nuevo nodo con el mismo dato
            if nueva_lista.cabeza is None:
                nueva_lista.cabeza = nuevo_nodo
                nueva_lista.cola = nuevo_nodo
            else:
                nueva_lista.cola.siguiente = nuevo_nodo
                nuevo_nodo.anterior = nueva_lista.cola
                nueva_lista.cola = nuevo_nodo
            actual = actual.siguiente
        nueva_lista.tamanio = self.tamanio
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
        copia_otra_lista = otra_lista.copiar()

        if self.cola is None:  # Si la lista actual está vacía
            self.cabeza = copia_otra_lista.cabeza
            self.cola = copia_otra_lista.cola
            self.tamanio = copia_otra_lista.tamanio
        else:
            self.cola.siguiente = copia_otra_lista.cabeza
            if copia_otra_lista.cabeza:
                copia_otra_lista.cabeza.anterior = self.cola
                self.cola = copia_otra_lista.cola
                self.tamanio += copia_otra_lista.tamanio

        return self
    
    def __add__(self, otra_lista):
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista
    
if __name__ == "__main__":

    NuevoValor = 25
    lista = ListaDoblementeEnlazada()
    lista2 = ListaDoblementeEnlazada()
    for i in range(5):
        lista.agregar_al_final(i)
    for i in range(5):
        lista2.agregar_al_final(i)
    lista.concatenar(lista2)
    lista2.mostrar_lista()
    print(lista2.cabeza.anterior)