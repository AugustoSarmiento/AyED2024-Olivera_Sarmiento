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
