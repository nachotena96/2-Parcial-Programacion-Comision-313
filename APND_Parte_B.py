#Parte B - Razonamiento 

# 1) Explique por que utilizar multiples listas separadas para almacenar datos relacionados puede generar errores de consistencia. 
# 2) Explique que ventajas aporta utilizar una estructura basada en clave-valor para buscar informacion. 
# 3) Explique por que una estructura que no permite duplicados puede ser util en sistemas reales. 
# 4) Explique las diferencias entre almacenar datos: 
#Unicamente en memoria;  
#en archivos.  
#    En que situaciones utilizaria cada alternativa?


# 1) Utilizar multiples listas paralelas nos puede conducir a una equivocacion en la asignacion de algun dato/valor a una variable erroneo generando incordancias porque debemos mantener manualmente el mismo orden y la misma cantidad de elementos en todas ellas.


# En su lugar yo utilizaria un diccionario, ya que a una varible me permite asociarle multiples datos a una variable (o en este caso, clave) y tener toda la informacion mucho mas ordenada.


# 2) Nos aporta una busqueda mucho mas directa de lo que queremos encontrar mediante la utilizacion de la clave, junto con toda la informacion asociada a esa clave (facilita la organizacion y recuperacion de informacion relacionada).


# 3) En determinados casos puntuales una estructura con este tipo de caracteristicas puede llegar a ser util, por ejemplo: un viaje de campania con numerosos investigadores que quieren obtener el numero total de especies animales observadas sin repetir ninguna. Esta estructura nos facilitaria la tarea ya que elimina automaticamente el numero de especies repetidas.


# 4) La diferencia principal esta en la persistencia de los datos, es decir, si los datos se conservan o no despues de finalizar la ejecucion del programa.
# Almacenar los datos unicamente en memoria implica que los datos se guardan temporalmente mientras el programa esta en ejecucion, una vez cerramos el programa la informacion se pierde. (Por ejemplo: Cuando los datos no necesitan conservarse despues de finalizar el programa.)
# Almacenar datos en archivos implica guardar la informacion en un medio de almacenamiento de manera persistente. (Por ejemplo: Cuando necesitamos recuperar datos previamente ingresados.)