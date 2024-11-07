class MonticuloBinario:
    def __init__(self):
        self.__lis_mon = [0]  
        self.__tam = 0  

    @property
    def lis_mon(self):
        return self.__lis_mon

    @lis_mon.setter
    def lis_mon(self, value):
        self.__lis_mon = value

    @property
    def tam(self):
        return self.__tam

    @tam.setter
    def tam(self, value):
        self.__tam = value

    def infilt_arriba(self, i):
        while i // 2 > 0:
            if self.lis_mon[i] < self.lis_mon[i // 2]:
               
                tmp = self.lis_mon[i // 2]
                self.lis_mon[i // 2] = self.lis_mon[i]
                self.lis_mon[i] = tmp
            i = i // 2 

    def insertar(self, k):
        self.lis_mon.append(k) 
        self.tam += 1
        self.infilt_arriba(self.tam)  
    def infilt_abajo(self, i):
        while (i * 2) <= self.tam:
            hm = self.__hijo_min(i)  
            if self.lis_mon[i] > self.lis_mon[hm]:
                tmp = self.lis_mon[i]
                self.lis_mon[i] = self.lis_mon[hm]
                self.lis_mon[hm] = tmp
            i = hm  

    def __hijo_min(self, i):
        if i * 2 + 1 > self.tam:
            return i * 2
        else:
            if self.lis_mon[i * 2] < self.lis_mon[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminar_min(self):
        valorSacado = self.lis_mon[1] 
        self.lis_mon[1] = self.lis_mon[self.tam]
        self.tam -= 1
        self.lis_mon.pop()
        self.infilt_abajo(1) 
        return valorSacado

    def construir_monticulo(self, unaLista):
        i = len(unaLista) // 2
        self.tam = len(unaLista)
        self.lis_mon = [0] + unaLista[:]
        while i > 0:
            self.infilt_abajo(i)
            i -= 1
