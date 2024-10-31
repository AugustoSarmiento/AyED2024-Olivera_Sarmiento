# paciente.py

import datetime

class Paciente:
    def __init__(self, nivel_riesgo, hora_llegada):
        self._nivel_riesgo = nivel_riesgo
        self._hora_llegada = hora_llegada

    @property
    def nivel_riesgo(self):
        return self._nivel_riesgo

    @nivel_riesgo.setter
    def nivel_riesgo(self, nivel_riesgo):
        self._nivel_riesgo = nivel_riesgo

    @property
    def hora_llegada(self):
        return self._hora_llegada

    @hora_llegada.setter
    def hora_llegada(self, hora_llegada):
        self._hora_llegada = hora_llegada

    def __lt__(self, other):
        # Comparación por nivel de riesgo primero, luego por hora de llegada
        if self.nivel_riesgo == other.nivel_riesgo:
            return self.hora_llegada < other.hora_llegada
        return self.nivel_riesgo < other.nivel_riesgo

    def __repr__(self):
        return f"Paciente(Riesgo={self.nivel_riesgo}, Hora={self.hora_llegada})"

