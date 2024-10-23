import datetime
import time
import random
from monticulo import MinHeap
from paciente import Paciente

def triaje():
    n = 20  # cantidad de ciclos de simulación
    cola_de_espera = MinHeap()

    for i in range(n):
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
        print('-*-'*15)
        print('\n', fecha_y_hora, '\n')

        # Se crea un nuevo paciente
        paciente = Paciente()
        cola_de_espera.insert(paciente)

        # Atención de paciente en este ciclo: en el 50% de los casos
        if random.random() < 0.5 and not cola_de_espera.is_empty():
            paciente_atendido = cola_de_espera.extract_min()
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)

        print('Pacientes que faltan atenderse:', len(cola_de_espera.heap))
        for paciente in cola_de_espera.heap:
            print('\t', paciente)
        
        print()
        print('-*-'*15)
        time.sleep(1)

if __name__ == "__main__":
    triaje()
