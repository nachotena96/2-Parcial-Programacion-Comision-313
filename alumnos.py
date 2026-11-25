from validaciones import pedir_texto, pedir_entero, pedir_documento, pedir_edad, pedir_nota_final


# Utilizamos range principalmente cuando necesitamos repetir una acción una determinada cantidad de veces o cuando necesitamos acceder a los elementos mediante sus índices. Cuando solamente necesitamos obtener los elementos, podemos recorrer el objeto directamente, sin utilizar range.
def buscar_documento(diccionario_alumnos: dict[int, dict[str, str | int]], documento: int) -> int | None:
    """
    Busca un alumno registrado en el diccionario mediante su número de documento.

    Recorre las claves del diccionario, que corresponden a los documentos
    de los alumnos registrados, y compara cada una con el documento recibido.

    Si encuentra una coincidencia, devuelve el número de documento correspondiente.

    Si finaliza el recorrido sin encontrar coincidencias, devuelve None.
    """

    for i in diccionario_alumnos:
        if i == documento:
            return i

    return None





def registrar_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> dict[int, dict[str, str | int]]:
    """
    Registra una cantidad determinada de alumnos en el diccionario.

    Solicita la cantidad de alumnos que se desean registrar y, para cada uno,
    pide su DNI, nombre, apellido, edad y nota final.

    Verifica que el DNI no se encuentre registrado previamente y valida los
    datos ingresados antes de almacenarlos en el diccionario.

    Retorna el diccionario actualizado con los nuevos alumnos registrados.
    """

    print("\n-. Registrar Alumnos .-")

    cantidad = pedir_entero("Ingrese la cantidad de alumnos que desea registrar: ")

    for i in range(cantidad):
        documento = pedir_documento("Ingrese el DNI del alumno: ")

        while buscar_documento(diccionario_alumnos, documento) is not None:
            print("- El DNI ingresado ya existe.")
            documento = pedir_documento("Ingrese el DNI del alumno: ")

        nombre = pedir_texto("Ingrese el nombre del alumno: ")
        apellido = pedir_texto("Ingrese el apellido del alumno: ")
        edad = pedir_edad("Ingrese la edad del alumno: ")
        nota = pedir_nota_final("Ingrese la nota final del alumno: ")

        diccionario_alumnos[documento] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota": nota
        }

        print("- Alumno registrado con éxito.")

    print("\n- Registro de alumnos terminado.")

    return diccionario_alumnos





def listar_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> None:
    """
    Muestra por pantalla el listado completo de alumnos registrados.

    Comprueba si el diccionario contiene alumnos. Si está vacío, informa
    que no se encontraron registros.

    Si existen alumnos registrados, recorre el diccionario y muestra
    los datos de cada uno: DNI, nombre, apellido, edad y nota final.

    No retorna ningún valor.
    """

    if len(diccionario_alumnos) == 0:
        print("No se han encontrado alumnos registrados.")
        return

    print("\n-. Listado de Alumnos .-")

    for documento in diccionario_alumnos:

        alumno = diccionario_alumnos[documento]

        print("------------------------------")
        print(f"Documento: {documento}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota final: {alumno['nota']}")

    print("------------------------------")





def buscar_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> None:
    """
    Busca un alumno registrado en el diccionario mediante su DNI.

    Comprueba si existen alumnos registrados. Si el diccionario está vacío,
    informa que no hay registros disponibles.

    Si existen alumnos, solicita el DNI del alumno que se desea buscar y
    verifica si se encuentra registrado.

    Si encuentra una coincidencia, muestra por pantalla los datos del alumno:
    DNI, nombre, apellido, edad y nota final.

    Si no encuentra el DNI ingresado, informa que el alumno no está registrado.

    No retorna ningún valor.
    """

    if len(diccionario_alumnos) == 0:
        print("No se han encontrado alumnos registrados.")
        return

    dni = pedir_documento("Ingrese el DNI del alumno que desea buscar: ")

    dni_encontrado = buscar_documento(diccionario_alumnos, dni)

    if dni_encontrado is not None:
        alumno = diccionario_alumnos[dni_encontrado]

        print("\n-. Alumno encontrado .-")
        print("------------------------------")
        print(f"DNI: {dni_encontrado}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota final: {alumno['nota']}")
        print("------------------------------")

        return

    print("- No se encontró ningún alumno con el DNI ingresado.")





def modificar_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> dict[int, dict[str, str | int]]:
    """
    Modifica los datos de un alumno previamente registrado en el diccionario.

    Comprueba si existen alumnos registrados. Si el diccionario está vacío,
    informa que no hay registros disponibles.

    Si existen alumnos, solicita el DNI del alumno que se desea modificar
    y verifica que se encuentre registrado.

    Si encuentra una coincidencia, solicita nuevamente el nombre, apellido,
    edad y nota final del alumno, reemplazando sus datos anteriores por los
    nuevos valores ingresados.

    Si el DNI no existe, informa que no se encontró el alumno solicitado.

    Retorna el diccionario actualizado con las modificaciones realizadas.
    """

    if len(diccionario_alumnos) == 0:
        print("No se han encontrado alumnos registrados.")
        return diccionario_alumnos

    documento = pedir_documento("Ingrese el DNI del alumno que desea MODIFICAR: ")

    documento_encontrado = buscar_documento(diccionario_alumnos, documento)

    if documento_encontrado is not None:

        nombre_nuevo = pedir_texto("Ingrese el nuevo nombre del alumno: ")
        apellido_nuevo = pedir_texto("Ingrese el nuevo apellido del alumno: ")
        edad_nueva = pedir_edad("Ingrese la nueva edad del alumno: ")
        nota_nueva = pedir_nota_final("Ingrese la nueva nota final del alumno: ")

        diccionario_alumnos[documento_encontrado] = {
            "nombre": nombre_nuevo,
            "apellido": apellido_nuevo,
            "edad": edad_nueva,
            "nota": nota_nueva
        }

        print("- Alumno modificado exitosamente.")

    else:
        print("- No se encontró ningún alumno con el DNI ingresado.")

    return diccionario_alumnos





def eliminar_alumnos(diccionario_alumnos: dict[int, dict[str, str | int]]) -> dict[int, dict[str, str | int]]:
    """
    Elimina un alumno del diccionario mediante su número de documento.

    Comprueba si existen alumnos registrados. Si el diccionario está vacío,
    informa que no hay registros disponibles.

    Si existen alumnos, solicita el DNI del alumno que se desea eliminar
    y verifica que se encuentre registrado.

    Si encuentra una coincidencia, elimina el registro completo del alumno,
    incluyendo su nombre, apellido, edad y nota final.

    Si el DNI no existe, informa que no se encontró el alumno solicitado.

    Retorna el diccionario actualizado sin el registro del alumno eliminado.
    """

    if len(diccionario_alumnos) == 0:
        print("No se han encontrado alumnos registrados.")
        return diccionario_alumnos

    documento = pedir_documento("Ingrese el DNI del alumno que desea ELIMINAR: ")

    documento_encontrado = buscar_documento(diccionario_alumnos, documento) # Recorre el diccionario buscando un documento en las claves 

    if documento_encontrado is not None:
        del diccionario_alumnos[documento_encontrado]

        print("- Alumno eliminado exitosamente.")

    else:
        print("- No se encontró ningún alumno con el DNI ingresado.")

    return diccionario_alumnos


