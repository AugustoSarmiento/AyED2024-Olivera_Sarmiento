import random
import modules
import time
import modules.AlgoritmosDeOrdenamiento

lista =[]
for i in range(500):
    x= random.randint(10000,99999)
    lista.append(x)

print(modules.AlgoritmosDeOrdenamiento.bubble_sort(lista))
print(modules.AlgoritmosDeOrdenamiento.quick_sort(lista))
print(modules.AlgoritmosDeOrdenamiento.radix_sort(lista))

lista_prueba = []
for i in range (10):
    x= random.randint(1,15)
    lista_prueba.append(x)
    print(lista_prueba)
    