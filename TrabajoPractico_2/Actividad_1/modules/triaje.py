class NodoABB:
    def __init__(self, clave, valor):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = None

    def esHoja(self):
        return self.hijoIzquierdo is None and self.hijoDerecho is None

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        return self.hijoDerecho is not None

    def tieneAmbosHijos(self):
        return self.hijoIzquierdo is not None and self.hijoDerecho is not None

    def reemplazarDato(self, clave, valor, hi=None, hd=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hi
        self.hijoDerecho = hd
        if self.hijoIzquierdo is not None:
            self.hijoIzquierdo.padre = self
        if self.hijoDerecho is not None:
            self.hijoDerecho.padre = self


class ABB:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor):
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoABB(clave, valor)
        self.tamano += 1

    def _agregar(self, clave, valor, nodo_actual):
        if clave < nodo_actual.clave:
            if nodo_actual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodo_actual.hijoIzquierdo)
            else:
                nodo_actual.hijoIzquierdo = NodoABB(clave, valor)
                nodo_actual.hijoIzquierdo.padre = nodo_actual
        else:
            if nodo_actual.tieneHijoDerecho():
                self._agregar(clave, valor, nodo_actual.hijoDerecho)
            else:
                nodo_actual.hijoDerecho = NodoABB(clave, valor)
                nodo_actual.hijoDerecho.padre = nodo_actual

    def obtener(self, clave):
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                raise KeyError("Clave no encontrada en el árbol.")
        else:
            raise KeyError("Árbol vacío.")

    def _obtener(self, clave, nodo_actual):
        if nodo_actual is None:
            return None
        elif clave == nodo_actual.clave:
            return nodo_actual
        elif clave < nodo_actual.clave:
            return self._obtener(clave, nodo_actual.hijoIzquierdo)
        else:
            return self._obtener(clave, nodo_actual.hijoDerecho)

    def eliminar(self, clave):
        if self.tamano > 1:
            nodo_a_eliminar = self._obtener(clave, self.raiz)
            if nodo_a_eliminar:
                self._eliminar_nodo(nodo_a_eliminar)
                self.tamano -= 1
            else:
                raise KeyError("Clave no encontrada en el árbol.")
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano -= 1
        else:
            raise KeyError("Clave no encontrada en el árbol.")

    def _eliminar_nodo(self, nodo):
        if nodo.esHoja():  # Caso 1: nodo hoja
            if nodo.padre:
                if nodo == nodo.padre.hijoIzquierdo:
                    nodo.padre.hijoIzquierdo = None
                else:
                    nodo.padre.hijoDerecho = None
            else:
                self.raiz = None
        elif nodo.tieneAmbosHijos():  # Caso 3: nodo con dos hijos
            sucesor = self._buscar_sucesor(nodo)
            nodo.reemplazarDato(sucesor.clave, sucesor.cargaUtil)
            self._eliminar_nodo(sucesor)
        else:  # Caso 2: nodo con un solo hijo
            if nodo.tieneHijoIzquierdo():
                if nodo.padre:
                    if nodo == nodo.padre.hijoIzquierdo:
                        nodo.padre.hijoIzquierdo = nodo.hijoIzquierdo
                    else:
                        nodo.padre.hijoDerecho = nodo.hijoIzquierdo
                    nodo.hijoIzquierdo.padre = nodo.padre
                else:
                    self.raiz = nodo.hijoIzquierdo
                    self.raiz.padre = None
            elif nodo.tieneHijoDerecho():
                if nodo.padre:
                    if nodo == nodo.padre.hijoIzquierdo:
                        nodo.padre.hijoIzquierdo = nodo.hijoDerecho
                    else:
                        nodo.padre.hijoDerecho = nodo.hijoDerecho
                    nodo.hijoDerecho.padre = nodo.padre
                else:
                    self.raiz = nodo.hijoDerecho
                    self.raiz.padre = None

    def _buscar_sucesor(self, nodo):
        sucesor = nodo.hijoDerecho
        while sucesor and sucesor.tieneHijoIzquierdo():
            sucesor = sucesor.hijoIzquierdo
        return sucesor

    def __contains__(self, clave):
        try:
            self.obtener(clave)
            return True
        except KeyError:
            return False

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)

    def __delitem__(self, clave):
        self.eliminar(clave)

    def __iter__(self):
        if self.raiz:
            return self._iter_in_order(self.raiz)
        else:
            return iter([])

    def _iter_in_order(self, nodo_actual):
        if nodo_actual:
            if nodo_actual.tieneHijoIzquierdo():
                yield from self._iter_in_order(nodo_actual.hijoIzquierdo)
            yield (nodo_actual.clave, nodo_actual.cargaUtil)
            if nodo_actual.tieneHijoDerecho():
                yield from self._iter_in_order(nodo_actual.hijoDerecho)

    def __len__(self):
        return self.tamano
