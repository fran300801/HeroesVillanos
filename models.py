import random
from datetime import date

class Persona():
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.identificador = identificador

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        # Si aún no ha cumplido años este año, se resta uno
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def __str__(self):
        return (f"{self.identificador} - {self.nombre} {self.apellidos} " 
                f"({self.calcular_edad()} años)")


class Villano(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.chatgepeteador = random.randint(0, 100)
        self.entregator_tardio = random.randint(0, 100)
        self.ausencias = random.randint(0, 100)
        self.hablador = random.randint(0, 100)
        self.puntuacion_total = self.calcular_media_villano()

    def calcular_media_villano(self):
        return (self.chatgepeteador + self.entregator_tardio + self.ausencias + self.hablador) / 4

    def obtener_cualidades(self):
        return {
            "chatgepeteador": self.chatgepeteador,
            "entregator_tardio": self.entregator_tardio,
            "ausencias": self.ausencias,
            "hablador": self.hablador,
        }

class Heroe(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.codigo_limpio = random.randint(0, 100)
        self.bien_documentado = random.randint(0, 100)
        self.gitgod = random.randint(0, 100)
        self.arquitecto = random.randint(0, 100)
        self.detalla = random.randint(0, 100)
        self.puntuacion_total = self.calcular_media_heroe()

    def calcular_media_heroe(self):
        return (self.codigo_limpio + self.bien_documentado + self.gitgod + self.arquitecto + self.detalla) / 5

    def obtener_cualidades(self):
        return {
            "codigo_limpio": self.codigo_limpio,
            "bien_documentado": self.bien_documentado,
            "gitgod": self.gitgod,
            "arquitecto": self.arquitecto,
            "detalla": self.detalla,
        }
