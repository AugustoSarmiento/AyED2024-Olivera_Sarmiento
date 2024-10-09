import time
import matplotlib as plt
from modules.ListasDoblementeEnlazadas import ListaDoblementeEnlazada
def medir_tiempo(func, *args, **kwargs):
    tiempo_inicio = time.time()
    resultado = func(*args, **kwargs)
    tiempo_fin = time.time()
    return resultado, tiempo_fin - tiempo_inicio



tamaños_de_listas = [100, 1000, 5000, 10000, 20000]
lista_tiempos_len = []
lista_tiempos_copiar = []
lista_tiempos_invertir = []

for i in tamaños_de_listas:
    dll = ListaDoblementeEnlazada()
    
    for j in range(i):
        dll.agregar_al_final(j)

    _, time_len = medir_tiempo(len, dll)
    copiar, tiempo_copiar = medir_tiempo(dll.copiar)
    dll.invertir()
    _, tiempo_invertir = medir_tiempo(len, dll) 

    lista_tiempos_len.append(time_len)
    lista_tiempos_copiar.append(tiempo_copiar)
    lista_tiempos_invertir.append(tiempo_invertir)


plt.plot(tamaños_de_listas, lista_tiempos_len, label='len')
plt.plot(tamaños_de_listas, lista_tiempos_copiar, label='copiar')
plt.plot(tamaños_de_listas, lista_tiempos_invertir, label='invertir')
plt.xlabel('Número de elementos (N)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Complejidad de operaciones en lista doblemente enlazada')
plt.legend()
plt.show()
