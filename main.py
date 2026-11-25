from alumnos import (
    registrar_alumnos,
    listar_alumnos,
    buscar_alumnos,
    modificar_alumnos,
    eliminar_alumnos
)

from estadisticas import mostrar_estadisticas

from archivos import cargar_alumnos, guardar_alumnos


mostrar_menu = False

diccionario_alumnos = cargar_alumnos()


while not mostrar_menu:
      print("...GESTIÓN DE ALUMNOS...")
      print("1. Registrar Alumno. ")
      print("2. Listar Alumno. ")
      print("3. Buscar Alumno. ")
      print("4. Modificar Alumno. ")
      print("5. Eliminar Alumno. ")
      print("6. Ver Estadisticas. ")
      print("7. Salir. ")

      opcion = input("Seleccione una opción del menu: ")

      match opcion:
            case "1":
                  registrar_alumnos(diccionario_alumnos)
                  guardar_alumnos(diccionario_alumnos)
            case "2":
                  listar_alumnos(diccionario_alumnos)                  
            case "3":
                  buscar_alumnos(diccionario_alumnos)
            case "4":
                  modificar_alumnos(diccionario_alumnos)
                  guardar_alumnos(diccionario_alumnos)
            case "5":
                  eliminar_alumnos(diccionario_alumnos)
                  guardar_alumnos(diccionario_alumnos)
            case "6":
                  mostrar_estadisticas(diccionario_alumnos)
                  guardar_alumnos(diccionario_alumnos)
            case "7":
                  print("Saliendo del Programa...")
                  mostrar_menu = True
            case _:
                  print("Opción inválida. Por favor, seleccione una opción correcta. (1 - 7)")
                  
