class MinHeap:
    def __init__(self):
        self.__heap = []

    @property
    def heap(self):
        return self.__heap

    def insert(self, paciente):
        self.__heap.append(paciente)
        self.__heapify_up(len(self.__heap) - 1)

    def extract_min(self):
        if len(self.__heap) == 0:
            return None
        if len(self.__heap) == 1:
            return self.__heap.pop()
        
        root = self.__heap[0]
        self.__heap[0] = self.__heap.pop()
        self.__heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.__heap[index].riesgo < self.__heap[parent].riesgo:
            self.__heap[index], self.__heap[parent] = self.__heap[parent], self.__heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.__heap) and self.__heap[left].riesgo < self.__heap[smallest].riesgo:
            smallest = left
        if right < len(self.__heap) and self.__heap[right].riesgo < self.__heap[smallest].riesgo:
            smallest = right

        if smallest != index:
            self.__heap[index], self.__heap[smallest] = self.__heap[smallest], self.__heap[index]
            self._heapify_down(smallest)

    def is_empty(self):
        return len(self.__heap) == 0
