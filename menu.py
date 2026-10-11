import logging

logger = logging.getLogger(__name__)


def mostrar_menu():
    print("\n--- HÉROES Y VILLANOS ---")
    print("1. Crear héroe")
    print("2. Crear villano")
    print("3. Listar personas")
    print("4. Buscar")
    print("5. Emparejar héroe y villano")
    print("0. Salir")
    return input("Elige una opción: ")


def mostrar_personas(lista):
    if not lista:
        print("  (sin resultados)")
    for p in lista:
        print(" ", p)
        for nombre, valor in p.obtener_cualidades().items():
            print(f"{nombre.replace('_', ' ')}: {valor}")
        print(f"puntuación total: {p.puntuacion_total:.2f}")


def mostrar_emparejamiento(datos):
    if datos is None:
        print("Necesitas al menos un héroe y un villano.")
        return
    heroe, villano, diferencia, resultado = datos
    print(f"Héroe: {heroe} -> {heroe.puntuacion_total:.2f}")
    print(f"Villano: {villano} -> {villano.puntuacion_total:.2f}")
    print(f"Diferencia: {diferencia:.2f} -> {resultado}")


def pedir_busqueda():
    tipo = ""
    while tipo != "h" and tipo != "v":
        tipo = input("¿Héroes o villanos? (h/v): ").lower().strip()
        if tipo != "h" and tipo != "v":
            print("Introduce un valor correcto: h (héroe) o v (villano).")

    if tipo == "h":
        tipo = "heroe"
    else:
        tipo = "villano"
    atributo = input("Atributo (nombre, edad, gitgod, ausencias...): ").lower()
    operador = input("Operador (=, !=, >, <, >=, <=): ")
    valor = input("Valor: ")
    return tipo, atributo, operador, valor


def ejecutar(controlador):
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            print("Creado:", controlador.crear("heroe"))
        elif opcion == "2":
            print("Creado:", controlador.crear("villano"))
        elif opcion == "3":
            mostrar_personas(controlador.listar())
        elif opcion == "4":
            try:
                resultados = controlador.buscar(*pedir_busqueda())
                mostrar_personas(resultados)
            except ValueError:
                logger.exception("Error en la búsqueda")
                print("Búsqueda no válida: revisa el valor y el operador.")
        elif opcion == "5":
            mostrar_emparejamiento(controlador.emparejar())
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")