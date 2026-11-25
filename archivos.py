
import json

NOMBRE_ARCHIVO = "alumnos.json"


def cargar_alumnos() -> dict[int, dict[str, str | int]]:
    """
    Carga los datos de los alumnos almacenados en un archivo JSON.

    Abre el archivo en modo lectura y utiliza json.load() para recuperar
    los datos almacenados.

    Convierte las claves del diccionario, que representan los DNI de los
    alumnos, de cadenas de texto a números enteros.

    Retorna el diccionario con los datos de los alumnos cargados en memoria.
    """
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
        diccionario_alumnos = json.load(archivo)

    for dni in list(diccionario_alumnos.keys()):
        diccionario_alumnos[int(dni)] = diccionario_alumnos.pop(dni)

    return diccionario_alumnos





def guardar_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> None:
    """
    Guarda los datos de los alumnos registrados en un archivo JSON.

    Abre el archivo en modo escritura y utiliza json.dumps() para convertir
    el diccionario de alumnos en una cadena de texto con formato JSON.

    Luego, escribe el contenido generado en el archivo, reemplazando
    la información que estuviera almacenada anteriormente.

    No retorna ningún valor.
    """

    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        texto_json = json.dumps(diccionario_alumnos, indent=4)
        archivo.write(texto_json)