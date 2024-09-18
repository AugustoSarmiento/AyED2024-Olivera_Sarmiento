class DequeEmptyError(Exception):
    """Excepción personalizada para mazos vacíos."""
    pass


class Carta:
    """Clase que representa un Carta de una lista doblemente enlazada."""
    def __init__(self, carta=None):
        self.carta = carta
        self.siguiente = None
        self.anterior = None


class Mazo:
    """Clase que representa un mazo de cartas utilizando una lista doblemente enlazada."""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._size = 0

    def __len__(self):
        """Retorna el número de cartas en el mazo."""
        return self._size

    def __str__(self):
        """Imprime las cartas del mazo desde la cabeza a la cola."""
        actual = self.cabeza
        cartas = []
        while actual:
            cartas.append(str(actual.carta))
            actual = actual.siguiente
        return " ".join(cartas)

    def poner_carta_arriba(self, carta):
        """Coloca una carta al principio del mazo (arriba)."""
        nuevo_Carta = Carta(carta)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_Carta
        else:
            nuevo_Carta.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_Carta
            self.cabeza = nuevo_Carta
        self._size += 1

    def poner_carta_abajo(self, carta):
        """Coloca una carta al final del mazo (abajo)."""
        nuevo_Carta = Carta(carta)
        if self.cola is None:
            self.cabeza = self.cola = nuevo_Carta
        else:
            nuevo_Carta.anterior = self.cola
            self.cola.siguiente = nuevo_Carta
            self.cola = nuevo_Carta
        self._size += 1

    def sacar_carta_arriba(self):
        """Saca una carta del principio del mazo (arriba)."""
        if self.cabeza is None:
            raise DequeEmptyError("El mazo está vacío.")
        carta = self.cabeza.carta
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self._size -= 1
        return carta

    def sacar_carta_abajo(self):
        """Saca una carta del final del mazo (abajo)."""
        if self.cola is None:
            raise DequeEmptyError("El mazo está vacío.")
        carta = self.cola.carta
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self._size -= 1
        return carta