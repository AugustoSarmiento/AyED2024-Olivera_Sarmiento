import random

class DequeEmptyError(Exception):
    """Excepción personalizada para mazos vacíos."""
    pass


class Carta:
    """Clase que representa una dato con valor y palo."""
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __gt__(self, otra):
        """Compara dos datos basadas en su valor."""
        return Carta.valores.index(self.valor) > Carta.valores.index(otra.valor)

    def __lt__(self, otra):
        """Compara si la dato actual es menor que otra."""
        return Carta.valores.index(self.valor) < Carta.valores.index(otra.valor)

    def __eq__(self, otra):
        """Verifica si dos datos tienen el mismo valor."""
        return Carta.valores.index(self.valor) == Carta.valores.index(otra.valor)

    def __str__(self):
        """Devuelve la representación en cadena de una dato."""
        return f'{self.valor} de {self.palo}'


class Nododato:
    """Nodo que representa una dato en una lista doblemente enlazada."""
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class Mazo:
    """Clase que representa un mazo de datos utilizando una lista doblemente enlazada."""
    def __init__(self):
        self.mazo = self
        self.cabeza = None
        self.cola = None
        self._size = 0
        self.crear_mazo()
        

    def crear_mazo(self):
        """Genera el mazo estándar de 52 datos con 4 palos y 13 valores."""
        palos = ['♠', '♥', '♦', '♣']
        valores = Carta.valores
        for palo in palos:
            for valor in valores:
                dato = Carta(valor, palo)
                self.poner_carta_abajo(dato)
        random.shuffle(self._mazo_como_lista())  # Mezcla las datos generadas

    def _mazo_como_lista(self):
        """Convierte el mazo en una lista de datos para mezclarlas."""
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def __len__(self):
        """Retorna el número de datos en el mazo."""
        return self._size

    def poner_carta_arriba(self, dato):
        """Coloca una dato al principio del mazo (arriba)."""
        nuevo_nodo = Nododato(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self._size += 1

    def poner_carta_abajo(self, dato):
        """Coloca una dato al final del mazo (abajo)."""
        nuevo_nodo = Nododato(dato)
        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self._size += 1

    def sacar_carta_arriba(self):
        """Saca una dato del principio del mazo (arriba)."""
        if self.cabeza is None:
            raise DequeEmptyError("El mazo está vacío.")
        dato = self.cabeza.dato
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self._size -= 1
        return dato

    def sacar_dato_abajo(self):
        """Saca una dato del final del mazo (abajo)."""
        if self.cola is None:
            raise DequeEmptyError("El mazo está vacío.")
        dato = self.cola.dato
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self._size -= 1
        return dato

    def __str__(self):
        """Imprime las datos del mazo desde la cabeza a la cola."""
        actual = self.cabeza
        datos = []
        while actual:
            datos.append(str(actual.dato))
            actual = actual.siguiente
        return " ".join(datos)

class JuegoGuerra:
    """Clase que simula el juego de la Guerra entre dos jugadores."""
    def __init__(self, random_seed=None):
        self.mazo_completo = Mazo()  # Crea un mazo completo y lo mezcla
        self.jugador1 = []
        self.jugador2 = []
        self.turnos_jugados = 0
        self.ganador = None
        self.empate = False
        if random_seed is not None:
            random.seed(random_seed)
        self.repartir_cartas()

    def repartir_cartas(self):
        """Reparte las cartas del mazo entre los dos jugadores."""
        while len(self.mazo_completo) > 0:
            self.jugador1.append(self.mazo_completo.sacar_carta_arriba())
            if len(self.mazo_completo) > 0:
                self.jugador2.append(self.mazo_completo.sacar_carta_arriba())

    def iniciar_juego(self, ver_partida=False):
        """Inicia la partida simulando turnos hasta que un jugador gane o haya empate."""
        while len(self.jugador1) > 0 and len(self.jugador2) > 0:
            self.turnos_jugados += 1
            carta_jugador1 = self.jugador1.pop(0)
            carta_jugador2 = self.jugador2.pop(0)

            if carta_jugador1 > carta_jugador2:
                self.jugador1.extend([carta_jugador1, carta_jugador2])  # Gana jugador 1
            elif carta_jugador2 > carta_jugador1:
                self.jugador2.extend([carta_jugador1, carta_jugador2])  # Gana jugador 2
            else:
                # En caso de empate, las cartas se descartan
                continue

        # Determinar ganador o empate
        if len(self.jugador1) > len(self.jugador2):
            self.ganador = 'jugador 1'
        elif len(self.jugador2) > len(self.jugador1):
            self.ganador = 'jugador 2'
        else:
            self.empate = True