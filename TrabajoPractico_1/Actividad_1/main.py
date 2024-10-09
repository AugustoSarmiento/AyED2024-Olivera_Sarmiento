from modules.AlgoritmosDeOrdenamiento import bubble_sort
from modules.AlgoritmosDeOrdenamiento import quick_sort
from modules.AlgoritmosDeOrdenamiento import radix_sort

import random
import time
import matplotlib as plt 
def medir_tiempos():
    tamaños = range(1, 1001)
    tiempos_burbuja = []
    tiempos_quicksort = []
    tiempos_radix = []
    tiempos_sorted = []

    for tamaño in tamaños:
        lista = [random.randint(10000, 99999) for _ in range(tamaño)]

        inicio = time.time()
        bubble_sort(lista.copy())
        tiempos_burbuja.append(time.time() - inicio)

        inicio = time.time()
        quick_sort(lista.copy())
        tiempos_quicksort.append(time.time() - inicio)

        inicio = time.time()
        radix_sort(lista.copy())
        tiempos_radix.append(time.time() - inicio)

        inicio = time.time()
        sorted(lista.copy())
        tiempos_sorted.append(time.time() - inicio)

    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_burbuja, label='Burbuja')
    plt.plot(tamaños, tiempos_quicksort, label='Quicksort')
    plt.plot(tamaños, tiempos_radix, label='Radix Sort')
    plt.plot(tamaños, tiempos_sorted, label='sorted')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend()
    plt.show()

medir_tiempos()
