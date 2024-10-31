# triaje.py

import random
import datetime
import time
from modules.min_heap import MinHeap
from modules.paciente import Paciente

def generar_paciente():
    nivel_riesgo = random.randint(1, 3)
    ahora = datetime.datetime.now()
    hora_llegada = ahora.strftime('%d/%m/%Y %H:%M:%S')
    return Paciente(nivel_riesgo, hora_llegada)

def simular_triaje():
    heap_pacientes = MinHeap()
    ciclos = 10  # número de ciclos de la simulación

    for i in range(ciclos):
        print(f"\n{'-'*10} Ciclo {i+1} {'-'*10}")

        # Generación y almacenamiento de un nuevo paciente
        nuevo_paciente = generar_paciente()
        print(f"[NUEVO PACIENTE] Generado: {nuevo_paciente}")
        heap_pacientes.insert(nuevo_paciente)

        # Mostrar el estado del montículo después de insertar el nuevo paciente
        heap_pacientes.mostrar_heap()

        # Probabilidad de atender a un paciente en el ciclo
        if random.random() < 0.5 and not heap_pacientes.is_empty():
            paciente_atendido = heap_pacientes.extract_min()
            print(f"[ATENCIÓN] Paciente atendido: {paciente_atendido}")
            print(f"Razón: Prioridad {paciente_atendido.nivel_riesgo} y llegada el {paciente_atendido.hora_llegada}")
        else:
            print("[INFO] No se atiende paciente en este ciclo.")

        # Mostrar el estado del montículo después de la atención
        heap_pacientes.mostrar_heap()
        
        time.sleep(1)
