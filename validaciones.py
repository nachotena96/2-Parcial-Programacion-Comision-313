def validar_textos(texto: str) -> bool:
    """
    Valida que un texto contenga únicamente letras y espacios, y que no esté vacío.
    """

    for i in range(len(texto)):
        caracter = texto[i]
        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z"
        espacio = caracter == " "

        if not (minuscula or mayuscula or espacio):
            return False

    return texto.strip() != "" # verifica que no tenga espacios vacios (al principio y al final) y sea distinto de espacio vacios. si se cumple retorna TRUE



def validar_entero_no_negativo(texto: str) -> bool:
    """
    Valida que el texto no esté vacío y contenga únicamente dígitos del 0 al 9.
    """

    valido = True

    if texto == "": #primero se fija que no este vacio
        print("- No ingreso ningun numero. ")
        return False

    for i in range(len(texto)): #despues se fija que sea un numero entre 0 y 9
        if texto[i] < "0" or texto[i] > "9":
            print("- El elemento ingresado debe ser un entero. Debe estar entre el 0 y el 9 (0 - 9). ")

            return False

    return True



def pedir_texto(mensaje: str) -> str: #si sale falso imprime el mensaje de que el campo no puede estar vacio y lo pide nuevamente hasta que validar texto retorne true
    """
    Solicita un texto y vuelve a pedirlo hasta que cumpla con las condiciones de validación.
    """

    texto = input(mensaje)

    while not validar_textos(texto):
        print("- El campo no puede estar vacio.")
        texto = input(mensaje)

    return texto



def pedir_entero(mensaje: str) -> int:
    """
    Solicita un número entero no negativo y vuelve a pedirlo hasta que sea válido.
    """

    texto = input(mensaje)

    while not validar_entero_no_negativo(texto):
        print("- Ingrese un numero entero valido y no negativo. ")
        texto = input(mensaje)

    return int(texto)



def pedir_documento(mensaje: str) -> int:
    """
    Solicita un número de documento y valida que tenga exactamente 8 dígitos.
    """

    documento = pedir_entero(mensaje)

    while documento < 10000000 or documento > 99999999:
        print("- Número de documento inválido. Debe contener 8 dígitos.")
        documento = pedir_entero(mensaje)

    return documento



def pedir_edad(mensaje: str) -> int:
    """
    Solicita una edad y valida que se encuentre entre 5 y 75 años.
    """

    edad = pedir_entero(mensaje)

    while edad < 5 or edad > 75:
        print("- Edad inválida. Debe estar comprendida entre 5 y 75 años.")
        edad = pedir_entero(mensaje)

    return edad



def pedir_nota_final(mensaje: str) -> int:
    """
    Solicita una nota final y valida que se encuentre entre 0 y 10.
    """

    nota = pedir_entero(mensaje)

    while nota < 0 or nota > 10:
        print("- Nota inválida. Debe estar comprendida entre 0 y 10.")
        nota = pedir_entero(mensaje)

    return nota


