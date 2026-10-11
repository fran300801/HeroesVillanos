import logging
from controlador import Controlador
import menu

logging.basicConfig(
    filename="heroes_villanos.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Programa iniciado")
    try:
        controlador = Controlador()
        controlador.crear_varios(10)  # creo 10 para no empezar con todo vacio
        menu.ejecutar(controlador)
    except Exception:
        logger.exception("Error inesperado")
        raise
    finally:
        logger.info("Programa finalizado")


if __name__ == "__main__":
    main()
