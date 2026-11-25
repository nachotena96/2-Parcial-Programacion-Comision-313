#Crear un diccionario que almacene los datos de tres alumnos. Cada alumno debe tener:
#- Nombre.
#- Apellido.
#- Edad.
#- Nota.

#Consignas:
#1. Crear el diccionario con tres alumnos.
#2. Mostrar el nombre y apellido de cada alumno.
#3. Buscar un alumno utilizando su documento.
#4. Calcular el promedio de las notas.
#5. Mostrar cuántos alumnos están registrados.
#Ejercicio 2. Inventario de productos
#
#Crear un diccionario para representar un inventario de productos.
#
#Cada producto tendrá:
#- Nombre.
#- Precio.
#- Stock.
#Consignas:
#1. Registrar cinco productos.
#2. Mostrar todos los productos.
#3. Buscar un producto por su código.
#4. Modificar el stock de un producto.
#5. Mostrar los productos cuyo stock sea inferior a 5 unidades.




#1)
alumnos = {
    "alumno1":{ 
        "nombre": "juancho",
        "apellido": "perez",
        "edad": 20,
        "nota": 8
            },    

    "alumno2": { 
        "nombre":"pepito",
        "apellido": "pc",
        "edad": 25,
        "nota": 10
                },

    "alumno3": {
        "nombre": "nacho",
        "apellido": "tena",
        "edad": 30,
        "nota": 10
                }
}

#2)
for alumno in alumnos.values():
    print(alumno["nombre"])
    print(alumno["apellido"])




nombre_buscado = input("Nombre del alumno buscado: ")

for alumno in alumnos.values():
    nombre = (alumno["nombre"])

    if nombre_buscado == nombre:
        print(f"el nombre buscado y encontrado es: {alumno["nombre"]}")



contador_nota = 0

for alumno in alumnos.values():
    nota = alumno["nota"]
    contador_nota = nota + contador_nota

total_alumnos= len(alumnos)

promedio = contador_nota / total_alumnos

print(f"el promedio es: {promedio}")




for alumno in alumnos:
    cantidad = len(alumnos)

print(cantidad)