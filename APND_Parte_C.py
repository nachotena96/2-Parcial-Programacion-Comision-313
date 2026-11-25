# Parte C - Analisis de codigo

#libro = ( "9789501234567", "Phython", "Guido", 2025)
#libro[1] = "Phython Avanzado"

# 1) El codigo funcionara? No, el codigo no funcionara.

# 2) Que ocurrira? Nos dara como resultado un ERROR.

# 3) Por que? Porque creamos una tupla y luego intentamos reasignar un valor  

# 4) Que caracteristica de la estructura utilizada produce ese comportamiento? La caracteristica es la INMUTABILIDAD 



#socios = {"Juan", "Ana", "Pedro", "Ana"}
#print(socios)

# 1) Cuántos elementos contendrá la estructura? La estructura contendra 3 elementos  

# 2) Por qué? Porque el elemento "Ana" se repite dos veces  

# 3) Qué ventaja aporta este comportamiento? Al tratarse de un CONJUNTO los elementos repetidos se eliminan automaticamente



#libros = {
    #"9789501234567": {
        #"titulo": "Python",
        #"autor": "Guido"
    #}
#}

# 1) Qué estructura de datos aparece en el ejemplo? En el ejemplo aparece un DICCIONARIO 

# 2) Qué representa cada clave? Tenemos dos diccionarios, uno externo y uno interno. La clave del diccionario externo representa la ISBN del librio (como si fuera un codigo de barras). El diccionario interno contiene las claves relacionadas a la informacion del libro, tales como el titulo de ese libro y el autor.

# #) Qué ventajas ofrece para realizar búsquedas? Nos permite realizar busqueda mucho mas directas a la vez que tenemos la informacion junto con los datos ordenados de manera organizada





# Un desarrollador afirma: 
# "Podría resolver todos los problemas utilizando únicamente listas." 

# Está de acuerdo con esta afirmación? 
#Justifique su respuesta indicando ventajas y desventajas de esa decisión. 

# Partiendo de la base de que es posible resolver todos los poblemas utilizando unicamente listas, no estoy de acuerdo con el desarrollador debido a que a medida que las listas se hacen mas extensas va a haber una mayor tendencia a realizar un error, como errores en la ubicación de los datos, pérdida de correspondencia entre elementos y mayor complejidad a la hora de administrar la información. Ahi es donde entran las demas estructuras de datos, los conjuntos evitan duplicados, los diccionarios permiten asociar información mediante claves y las tuplas permiten almacenar datos que no deben modificarse.





# Preguntas de selección múltiple 

# Respecto a los diccionarios en Python: 
# A) Permiten almacenar información mediante pares clave-valor. 
# B) Las claves deben ser únicas. 
# C) Los diccionarios mantienen el orden únicamente si se utiliza sorted(). 
# D) Se puede acceder a un valor utilizando su clave. 
# E) Los diccionarios no permiten almacenar otros diccionarios. 
# F) Son útiles para representar entidades como alumnos, libros o productos. 
#   RESPUESTAS CORRECTAS: A - B - D - F
  
  
 
# Respecto a las tuplas: 
  
# A) Son estructuras mutables. 
# B) Permiten almacenar distintos tipos de datos. 
# C) Una vez creadas, sus elementos no pueden modificarse. 
# D) Son adecuadas para representar información que no debería cambiar.
# E) Siempre ocupan más memoria que las listas.  (las tuplas son un poquito mas rapidas que las listas)
# F) Admiten acceso mediante índices.
#   RESPUESTAS CORRECTAS: B - C - D - F


 
# Respecto a los conjuntos (set): 
 
# A) Permiten elementos duplicados. 
# B) Son útiles para eliminar elementos repetidos. 
# C) No garantizan posiciones mediante índices. 
# D) Permiten acceder a sus elementos utilizando índices. 
# E) Son adecuados para representar colecciones de elementos únicos.  
# F) Mantienen necesariamente el orden de inserción. 
#   RESPUESTAS CORRECTAS: B - C - E 
 
  
 
# Respecto a las matrices en Python: 
 
# A) Generalmente se representan mediante listas anidadas. 
# B) Son adecuadas para modelar información organizada en filas y columnas.  
# C) Son una estructura nativa específica de Python llamada matrix.  
# D) No pueden recorrerse mediante ciclos. 
# E) Todos sus elementos deben ser del mismo tipo.  
# F) Permiten acceder a una posición utilizando fila y columna.
#   RESPUESTAS CORRECTAS: A - B - F
 
  
 
# Respecto al manejo de archivos: 
 
# A) Permite conservar información luego de finalizar la ejecución del programa. 
# B) El modo "r" se utiliza para lectura.  
# C) El modo "w" permite escribir en un archivo. 
# D) Los datos almacenados en archivos desaparecen cuando el programa finaliza.  
# E) La instrucción with open(...) ayuda a gestionar correctamente el cierre del archivo.  
# F) Los archivos solo pueden almacenar texto.
#   RESPUESTA CORRECTA: A - B - C - E




# Estructura elegida: DICCIONARIO.

# Almacenan pares clave-valor. Las claves deben ser unicas. 
ave = { 
    "nombre_comun": "Tijereta",
    "nombre_cientifico": "Tyrannus savana",
    "familia": "Tyrannidae" 
    }


# Podemos acceder a los valores utilizando sus respectivas claves. (ejemplo: ave["nombre_comun"]).
print("REGISTRO DE AVE")
print("-------------------------")

print("Nombre común:", ave["nombre_comun"]) #clave: nombre_comun
print("Nombre científico:", ave["nombre_cientifico"]) #clave: nombre_cientifico
print("Familia:", ave["familia"]) #clave: familia


# Podemos incorporar una clave nueva y su valor correspondiente.
ave["ambiente"] = "Pastizales y ambientes abiertos"

print("Ambiente:", ave["ambiente"])


# Podemos almacenar otro diccionario dentro del primero.
ave["ubicacion"] = {
    "provincia": "Buenos Aires",
    "pais": "Argentina"
}


# Juntos, ambos diccionarios quedarian asi: (medio confuso, yo lo agregaria como pares de clave-valor)
ave = {
    "nombre_comun": "Tijereta",
    "nombre_cientifico": "Tyrannus savana",
    "familia": "Tyrannidae",

    "ubicacion": {
        "provincia": "Buenos Aires",
        "pais": "Argentina"
    }
}


print("Provincia:", ave["ubicacion"]["provincia"])
print("Provincia:", ave["ubicacion"]["pais"])