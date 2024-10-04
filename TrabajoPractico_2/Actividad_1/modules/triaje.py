# -*- coding: utf-8 -*-
"""
Sala de emergencias con cola de prioridad
"""

import time
import datetime
import random
from modulos.paciente import Paciente
from cola_prioridad import ColaPrioridad  # Estructura de datos genérica

n = 20  # cantidad de ciclos de simulación
cola_de_espera = ColaPrioridad()  # Cola de prioridad para manejar los pacientes

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente()
    print(f'Nuevo paciente ingresado: {paciente}')

    # Se agrega el paciente a la cola con su nivel de prioridad (riesgo)
    cola_de_espera.agregar(paciente.nivel_riesgo, paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # Se atiende el paciente con mayor prioridad (menor nivel de riesgo)
        paciente_atendido = cola_de_espera.atender()
        if paciente_atendido:
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
        else:
            print('No hay pacientes para atender.')

    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.cantidad())
    print(cola_de_espera)

    print('-*-'*15)
    
    time.sleep(1)

