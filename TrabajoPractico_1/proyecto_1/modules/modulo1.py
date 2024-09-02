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

import random
lista_prueba=[]
for i in range(500):
  x= random.randint(10000,99999)
  lista_prueba.append(x)
print(lista_prueba)
print(bubble_sort(lista_prueba))
print(radix_sort(lista_prueba))


#consigna 2
class nodo:   #creo clase nodo
    def __init__(self,dato=None):
        self.dato= dato
        self.siguiente= None
        self.anterior= None

class listdoben: #creo lista doblemente enlazada 
    def __init__ (self):
        self.cabeza = None
        self.cola= None
        self.tamanio= 0 
