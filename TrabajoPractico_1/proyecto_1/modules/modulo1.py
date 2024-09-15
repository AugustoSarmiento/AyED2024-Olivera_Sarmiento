#consigna 1

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return(lista)

def quick_sort(lista):
    largo = len(lista)
    if largo <= 1:
        return lista
    else:
        pivote = lista.pop()
        
    mayores = []
    menores = []
    
    for i in lista:
        if i > pivote:
            mayores.append(i)
        
        else:
            menores.append(i)
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

def radix_sort(lista):
    max_num = max(lista)
    exp = 1

    while max_num / exp > 0:
        bloques = [[] for _ in range(10)]
        for i in lista:
            digito = (i // exp) % 10
            bloques[digito].append(i)
        lista = []
        for bloque in bloques:
            lista.extend(bloque)
        exp *= 10
    return lista


#consigna 2
class Nodo:
    def __init__(self, dato):
        self.data = dato
        self.prev = None
        self.next = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamanio =0

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo

        else:
            ultimo_nodo = self.cabeza
            while ultimo_nodo.next:
                ultimo_nodo = ultimo_nodo.next
            ultimo_nodo.next = nuevo_nodo

            nuevo_nodo.prev = ultimo_nodo
        self.tamanio +=1
    
    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            self.cabeza.prev = nuevo_nodo
            nuevo_nodo.next = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamanio+=1
            
    def mostrar_lista(self):
        cursor = self.cabeza
        while cursor:
            print(cursor.data, end=" ")
            cursor = cursor.next

    def esta_vacia(self): #si la lista está vacía, la cabeza no tiene valor
        if self.cabeza == None:
            return (print(True))
        else:
            return (print(False))
        
    def __len__(self):
        cant_elementos = self.tamanio
        return(print(cant_elementos))
    
    def insertar(self, dato, posicion=None):
        if posicion is None:
            self.agregar_al_final(dato)
            return
        if posicion < 0 or posicion > self.tamanio:
            raise ValueError("Posición fuera de rango")

        if posicion == 0:
            self.agregar_al_principio(dato)
            return

        if posicion == self.tamanio:
            self.agregar_al_final(dato)
            return

        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        for i in range(posicion - 1):
            actual = actual.next

        nuevo_nodo.prev = actual
        nuevo_nodo.next = actual.next
        actual.next.prev = nuevo_nodo
        actual.next = nuevo_nodo

        self.tamanio += 1
        
lista=ListaDoblementeEnlazada()
lista.esta_vacia()
lista.agregar_al_final(0)
lista.agregar_al_principio(4)
lista.agregar_al_principio(1)
lista.agregar_al_final(2)
lista.insertar(5,3)
lista.insertar(8)
lista.esta_vacia()
lista.__len__()
lista.mostrar_lista()