import random
import modules
import modules.AlgoritmosDeOrdenamiento

lista =[]
for i in range(500):
    x= random.randint(10000,99999)
    lista.append(x)
print
print(modules.AlgoritmosDeOrdenamiento.bubble_sort(lista))