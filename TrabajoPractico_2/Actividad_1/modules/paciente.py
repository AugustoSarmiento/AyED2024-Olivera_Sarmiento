from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']
niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6]

class Paciente:
    def __init__(self):
        self.__nombre = nombres[randint(0, len(nombres) - 1)]
        self.__apellido = apellidos[randint(0, len(apellidos) - 1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo - 1]

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def riesgo(self):
        return self.__riesgo

    @property
    def descripcion_riesgo(self):
        return self.__descripcion

    def __str__(self):
        return f"{self.__nombre} {self.__apellido} -> {self.__riesgo}-{self.__descripcion}"
