# min_heap.py

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)
        print(f"[INFO] Paciente agregado al montículo: {item}")

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def peek_min(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def mostrar_heap(self):
        if self.is_empty():
            print("[INFO] El montículo está vacío")
        else:
            print("[ESTADO DEL MONTÍCULO] Pacientes en el montículo:")
            for paciente in self.heap:
                print(f"\t- {paciente}")
            print()

