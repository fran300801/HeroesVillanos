import logging
import random
from faker import Faker
from models import Heroe, Villano

logger = logging.getLogger(__name__)
fake = Faker("es_ES")

UMBRAL_EQUILIBRIO = 15  # diferencia máxima para considerarlos equilibrados


def obtener_clase(tipo):
    if tipo == "heroe":
        return Heroe
    else:
        return Villano


def comparar(actual, operador, valor):
    if operador == "=":
        return actual == valor
    elif operador == "!=":
        return actual != valor
    elif operador == ">":
        return actual > valor
    elif operador == "<":
        return actual < valor
    elif operador == ">=":
        return actual >= valor
    elif operador == "<=":
        return actual <= valor
    else:
        logger.error(f"Operador no válido: {operador}")
        raise ValueError(f"Operador no válido: {operador}")


class Controlador:
    def __init__(self):
        self.personas = {}  # {identificador: persona}
        logger.info("Controlador iniciado")

    def crear(self, tipo):
        clase = obtener_clase(tipo)
        persona = clase(
            nombre=fake.first_name(),
            apellidos=f"{fake.last_name()} {fake.last_name()}",
            fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=40),
            identificador=fake.unique.bothify(text="ID-####"),
        )
        self.personas[persona.identificador] = persona
        logger.info(f"Creado {tipo} {persona.identificador} "
                    f"(puntuación {persona.puntuacion_total:.2f})")
        return persona

    def crear_varios(self, cantidad):
        for i in range(cantidad):
            self.crear(random.choice(["heroe", "villano"]))

    def listar(self, tipo=None):
        if tipo is None:
            return list(self.personas.values())
        clase = obtener_clase(tipo)
        return [p for p in self.personas.values() if isinstance(p, clase)]

    def buscar(self, tipo, atributo, operador, valor):
        logger.info(f"Búsqueda: {tipo} con {atributo} {operador} {valor}")
        resultados = []
        for p in self.listar(tipo):
            if atributo == "edad":
                actual = p.calcular_edad()
            elif hasattr(p, atributo):
                actual = getattr(p, atributo)
            else:
                continue
            try:
                if type(actual) == int or type(actual) == float:
                    valor_cmp = float(valor)
                else:
                    valor_cmp = valor.lower()
                    actual = str(actual).lower()
            except ValueError:
                logger.error(f"Valor no válido para {atributo}: {valor}")
                raise
            if comparar(actual, operador, valor_cmp):
                resultados.append(p)
        logger.info(f"Búsqueda terminada: {len(resultados)} resultados")
        return resultados

    def emparejar(self):
        heroes = self.listar("heroe")
        villanos = self.listar("villano")
        if not heroes or not villanos:
            logger.warning("No se puede emparejar: faltan héroes o villanos")
            return None

        heroe = random.choice(heroes)
        villano = random.choice(villanos)
        diferencia = abs(heroe.puntuacion_total - villano.puntuacion_total)

        if diferencia <= UMBRAL_EQUILIBRIO:
            resultado = "equilibrado"
        elif heroe.puntuacion_total < villano.puntuacion_total:
            resultado = "alta desviación: el villano es mucho más poderoso"
        else:
            resultado = "alta desviación: el héroe es mucho más poderoso"

        logger.info(f"Emparejamiento {heroe.identificador} vs "
                    f"{villano.identificador}: diferencia {diferencia:.2f} "
                    f"-> {resultado}")
        return heroe, villano, diferencia, resultado