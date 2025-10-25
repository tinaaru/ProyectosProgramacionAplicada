#################LISTAS####################
###########################################

# Se crea una lista llamada "my_lista" que contiene varios colores como elementos.
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  # Lista inicial de colores

# Muestra en pantalla todos los elementos de la lista.
print(my_lista)  # Imprime la lista completa

# Muestra el tipo de dato de la variable "my_lista".
print(type(my_lista))  # Devuelve <class 'list'>

# Muestra el elemento ubicado en el índice 2 (recordando que se empieza a contar desde 0).
print(my_lista[2])  # Muestra 'Amarillo'

# Muestra el número de elementos que tiene la lista usando len().
print("my_lista size: ", len(my_lista))  # Devuelve la longitud total de la lista (cantidad de colores)

# Muestra los elementos desde el índice 0 hasta el 1 (el 2 no se incluye).
print(my_lista[0:2])  # Muestra ['Rojo', 'Azul']

# Hace lo mismo que la anterior, omitiendo el 0 porque el inicio por defecto es 0.
print(my_lista[:2])  # Muestra ['Rojo', 'Azul']

# Agrega un nuevo color al final de la lista.
my_lista.append('Blanco')  # Añade 'Blanco' al final
print(my_lista)  # Muestra la lista actualizada

# Inserta un nuevo color ('Negro') en la posición 3 (entre 'Amarillo' y 'Naranja').
my_lista.insert(3, 'Negro')  # Inserta 'Negro' en la posición 3
print(my_lista)  # Muestra la lista con el nuevo elemento

# Agrega (extiende) otros elementos al final de la lista, en este caso 'Marron' y 'Gris'.
my_lista.extend(['Marron', 'Gris'])  # Combina ambas listas
print(my_lista)  # Muestra la lista extendida

# Busca y muestra la posición (índice) en la que se encuentra el color 'Azul'.
print(my_lista.index('Azul'))  # Devuelve el índice de 'Azul'

# Elimina el elemento 'Marron' de la lista.
# (La línea de arriba está comentada y no se ejecuta)
my_lista.remove('Marron')  # Elimina 'Marron' de la lista
print(my_lista)  # Muestra la lista actualizada sin 'Marron'

# Esta línea está entre comillas, por lo tanto, es una cadena de texto y no se ejecuta.
"my_lista.insert(8, 'Marron') #Insertar el color marron en la posicion 8 de la lista"
print(my_lista)  # Muestra la lista (sin cambios, ya que la línea anterior no se ejecutó)

# Elimina el último elemento de la lista y lo devuelve (lo imprime).
print(my_lista.pop())  # Quita el último color ('Gris') y lo muestra

# Calcula el tamaño (cantidad de elementos) actual de la lista.
size = len(my_lista)  # Guarda el número de elementos actuales
print("size = ", size)  # Muestra el tamaño de la lista

# Crea una nueva lista repitiendo tres veces todos los elementos de la lista original.
my_lista_3 = my_lista * 3  # Multiplica los elementos de la lista por 3
print("my_lista_3: ", my_lista_3)  # Muestra la nueva lista repetida

# Muestra el texto "Sort:" como encabezado.
print("Sort:")  # Imprime el título
print()  # Imprime una línea vacía para separar

# Ordena la lista original "my_lista" alfabéticamente (de forma ascendente).
my_listaSort = my_lista.sort()  # Ordena la lista en su lugar y devuelve None
print(my_listaSort)  # Muestra None (porque sort() no devuelve la lista ordenada, solo la modifica)

# Crea una nueva lista numérica del 10 al 1.
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  # Lista de números desordenados
print("Ordering my_NumList: ")  # Mensaje antes de ordenar

# Ordena la lista de números en orden ascendente (por defecto).
my_NumList.sort()  # Ordena los números de menor a mayor
print(my_NumList)  # Muestra la lista ordenada

# Ordena la lista en orden inverso (de mayor a menor).
my_NumList.sort(reverse=True)  # reverse=True cambia el orden a descendente
print("De menor a mayor: ", my_NumList)  # Muestra la lista en orden descendente



#################TUPLAS####################
###########################################

# Las tuplas son estructuras similares a las listas, pero no se pueden modificar.
# Es decir, son inmutables (una vez creadas, no se pueden cambiar).

# Se imprimen separadores visuales en pantalla.
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")

# Convierte la lista "my_lista" en una tupla.
my_tupla = tuple(my_lista)  # Transforma la lista en una tupla inmutable
print()  # Imprime una línea vacía
print()  # Imprime otra línea vacía
print("my_tuple: ", my_tupla)  # Muestra la tupla generada

# Muestra el primer elemento (índice 0) de la tupla.
print(my_tupla[0])  # Muestra el primer color

# Muestra el elemento que está en el índice 2 de la tupla.
print(my_tupla[2])  # Muestra el tercer color

# Verifica si el elemento 'Rojo' se encuentra en la tupla.
# Devuelve True si está, False si no.
print('Rojo' in my_tupla)  # Devuelve True si 'Rojo' está presente

# Cuenta cuántas veces aparece 'Rojo' en la tupla.
print(my_tupla.count('Rojo'))  # Devuelve el número de apariciones de 'Rojo'

# Crea una tupla con un solo elemento (aunque en realidad esto genera un string, no una tupla).
my_tupla_unitaria = ('Blanco')  # Sin coma, por lo que es un string
print(my_tupla_unitaria)  # Imprime 'Blanco'

# Crea una tupla mediante empaquetado, sin usar paréntesis.
my_tupla = 'Gaspar', 5, 8, 1999  # Empaqueta varios valores en una tupla
print(my_tupla)  # Muestra ('Gaspar', 5, 8, 1999)

# Desempaqueta la tupla asignando cada valor a una variable.
nombre, dia, mes, año = my_tupla  # Asigna en orden los valores
print(nombre)  # Imprime 'Gaspar'
print(dia)     # Imprime 5
print(mes)     # Imprime 8
print(año)     # Imprime 1999

# Imprime todos los valores desempaquetados en una sola línea formateada.
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convierte nuevamente la tupla en una lista.
my_lista2 = list(my_tupla)  # Crea una lista a partir de la tupla
print(my_lista2)  # Muestra la nueva lista
