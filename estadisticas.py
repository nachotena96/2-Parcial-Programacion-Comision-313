def mostrar_estadisticas(diccionario_alumnos: dict[int, dict[str, str | int]]) -> None:
    """
    Coordina la ejecución y visualización de las estadísticas de los alumnos registrados.

    Comprueba si existen alumnos en el diccionario. Si no hay registros,
    informa que no se pueden calcular las estadísticas y finaliza la ejecución.

    Si existen alumnos registrados, invoca las funciones encargadas de calcular
    y mostrar las siguientes estadísticas:

    - Cantidad total de alumnos registrados.
    - Promedio general de las notas.
    - Alumno con la nota más alta.
    - Cantidad de alumnos aprobados.
    - Cantidad de alumnos desaprobados.

    No retorna ningún valor.
    """

    print("\n-. Estadísticas .-")

    if len(diccionario_alumnos) == 0:
        print("No hay alumnos registrados.")
        return

    total_alumnos(diccionario_alumnos)
    promedio_notas(diccionario_alumnos)
    mostrar_alumno_mayor_nota(diccionario_alumnos)
    mostrar_aprobados(diccionario_alumnos)
    mostrar_desaprobados(diccionario_alumnos)
    




def total_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> int:
    """
    Calcula y muestra la cantidad total de alumnos registrados en el diccionario.

    Utiliza la función len() para obtener la cantidad de registros almacenados
    y muestra el resultado por pantalla.

    Retorna la cantidad total de alumnos como un número entero.
    """

    total_alumnos = len(diccionario_alumnos)

    print(f"La cantidad total de alumnos registrados es: {total_alumnos}")

    return total_alumnos





def promedio_notas(diccionario_alumnos: dict[int, dict[str, str | int]]) -> float:
    """
    Calcula y muestra el promedio general de las notas de los alumnos registrados.

    Recorre los valores del diccionario, obtiene la nota final de cada alumno
    y acumula todas las notas en una variable.

    Luego, divide la suma total de las notas por la cantidad de alumnos
    registrados para obtener el promedio general.

    Retorna el promedio calculado como un número decimal.
    """

    suma_notas = 0

    for alumno in diccionario_alumnos.values():
        nota = alumno["nota"]
        suma_notas = suma_notas + nota

    promedio_total = suma_notas / len(diccionario_alumnos)

    print(f"El promedio general de las notas es: {promedio_total}")

    return promedio_total



def mostrar_alumno_mayor_nota(diccionario_alumnos: dict[int, dict[str, str | int]]) -> dict[str, str | int] | None:
    """
    Busca y muestra los datos del alumno que obtuvo la mayor nota final.

    Recorre los valores del diccionario y compara las notas de cada alumno
    para identificar la calificación más alta.

    Si encuentra un alumno con una nota superior a la mayor registrada
    hasta el momento, actualiza el mejor alumno encontrado.

    Muestra por pantalla el DNI, nombre, apellido y nota del alumno
    que obtuvo la calificación más alta.

    Retorna el diccionario con los datos del alumno encontrado.
    Si no existen alumnos registrados, retorna None.
    """

    mejor_alumno = None

    for alumno in diccionario_alumnos.values():
        if mejor_alumno is None or alumno["nota"] > mejor_alumno["nota"]:
            mejor_alumno = alumno

    if mejor_alumno is None:
        print("No hay alumnos registrados.")
        return None

    print("\n-. Alumno con mayor nota .-")
    print(f"Nombre: {mejor_alumno['nombre']}")
    print(f"Apellido: {mejor_alumno['apellido']}")
    print(f"Nota final: {mejor_alumno['nota']}")

    return mejor_alumno





def mostrar_aprobados(diccionario_alumnos: dict[int, dict[str, str | int]]) -> int:
    """
    Calcula y muestra la cantidad de alumnos aprobados.

    Recorre los valores del diccionario y analiza la nota final de cada alumno.

    Considera aprobados a los alumnos que obtuvieron una nota igual o superior
    a 6. Por cada alumno que cumple esta condición, incrementa el contador.

    Retorna la cantidad total de alumnos aprobados como un número entero.
    """

    aprobados = 0

    for alumno in diccionario_alumnos.values():
        if alumno["nota"] >= 6:
            aprobados = aprobados + 1

    print(f"El número de alumnos aprobados es: {aprobados}")

    return aprobados





def mostrar_desaprobados(diccionario_alumnos: dict[int, dict[str, str | int]]) -> int:
    """
    Calcula y muestra la cantidad de alumnos desaprobados.

    Recorre los valores del diccionario y analiza la nota final de cada alumno.

    Considera desaprobados a los alumnos que obtuvieron una nota inferior a 6.
    Por cada alumno que cumple esta condición, incrementa el contador.

    Retorna la cantidad total de alumnos desaprobados como un número entero.
    """

    desaprobados = 0

    for alumno in diccionario_alumnos.values():
        if alumno["nota"] < 6:
            desaprobados += 1

    print(f"El número de alumnos desaprobados es: {desaprobados}")

    return desaprobados

