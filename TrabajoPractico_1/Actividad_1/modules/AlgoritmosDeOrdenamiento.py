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
