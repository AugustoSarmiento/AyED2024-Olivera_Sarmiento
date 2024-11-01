class MinHeap:
    def __init__(self):
        self.__heap = []

    def insert(self, item):
        self.__heap.append(item)
        self._sift_up(len(self.__heap) - 1)
        print(f"[INFO] Paciente agregado al montículo: {item}")

    def extract_min(self):
        if len(self.__heap) == 0:
            return None
        if len(self.__heap) == 1:
            return self.__heap.pop()
        
        min_item = self.__heap[0]
        # Mueve el último elemento al principio y ajusta el montículo
        self.__heap[0] = self.__heap.pop()
        self._sift_down(0)
        return min_item

    def peek_min(self):
        return self.__heap[0] if self.__heap else None

    def is_empty(self):
        return len(self.__heap) == 0

    def __len__(self):
        return len(self.__heap)

    def mostrar_heap(self):
        if self.is_empty():
            print("[INFO] El montículo está vacío")
        else:
            print("[ESTADO DEL MONTÍCULO] Pacientes en el montículo:")
            for paciente in self.__heap:
                print(f"\t- {paciente}")
            print()

    # Getters y setters para acceder al heap
    def get_heap(self):
        return self.__heap.copy()  # Devuelve una copia para evitar modificaciones directas

    def set_heap(self, new_heap):
        self.__heap = new_heap
        # Ajusta el heap desde el inicio en caso de ser necesario
        for i in reversed(range(len(self.__heap) // 2)):
            self._sift_down(i)

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.__heap[idx] < self.__heap[parent]:
            # Intercambia con el padre y continúa ajustando hacia arriba
            self.__heap[idx], self.__heap[parent] = self.__heap[parent], self.__heap[idx]
            self._sift_up(parent)

    def _sift_down(self, idx):
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx

        if left_child < len(self.__heap) and self.__heap[left_child] < self.__heap[smallest]:
            smallest = left_child
        if right_child < len(self.__heap) and self.__heap[right_child] < self.__heap[smallest]:
            smallest = right_child
        if smallest != idx:
            # Intercambia con el hijo menor y continúa ajustando hacia abajo
            self.__heap[idx], self.__heap[smallest] = self.__heap[smallest], self.__heap[idx]
            self._sift_down(smallest)
