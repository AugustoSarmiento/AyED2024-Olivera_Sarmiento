from modules.MontículoBinario import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()  
        self.posiciones = {}  
        self.elementos = set()

    def construir_monticulo(self, lista):
        self.monticulo.construir_monticulo(lista)  
        self.elementos = {v for _, v in lista}

    def insertar(self, clave, obj):

        self.monticulo.insertar((clave, obj))
        self.posiciones[obj] = self.monticulo.tam

    def eliminar_min(self):
        min_elemento = self.monticulo.eliminar_min() 
        self.elementos.remove(min_elemento[1]) 
        return min_elemento
        
    def decrementar_clave(self, obj, nueva_clave):
        index = self.posiciones.get(obj)
        if index is not None and nueva_clave < self.monticulo.lis_mon[index][0]:
            self.monticulo.lis_mon[index] = (nueva_clave, obj)
            self.monticulo.infilt_arriba(index)
            self.posiciones[obj] = index





    def esta_vacia(self):
        return self.monticulo.tam == 0

    def contiene(self, item):
        return item in self.elementos