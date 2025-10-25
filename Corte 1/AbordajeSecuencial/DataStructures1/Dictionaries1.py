# Se crea un diccionario llamado 'sensors' donde cada clave representa una habitación
# y el valor indica la cantidad de sensores instalados en ella.
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Se crea otro diccionario llamado 'num_cameras' con las zonas y el número de cámaras en cada una.
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Diccionario 'translations' que asocia palabras en inglés con sus traducciones en otro idioma inventado.
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# ❌ Este ejemplo genera error porque las listas no pueden usarse como claves en un diccionario.
# Las claves deben ser inmutables (no se pueden cambiar).
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

# Se crea un diccionario 'children' donde las claves son apellidos y los valores son listas de nombres.
children = {
    "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
    "Corleone": ["Sonny", "Fredo", "Michael"]
}

# Se imprime el contenido del diccionario 'children'.
print(children)

# Se crea un diccionario vacío llamado 'my_empty_dictionary'.
my_empty_dictionary = {}

# Se imprime el contenido del diccionario vacío ({}).
print(my_empty_dictionary)

# Diccionario 'menu' con los nombres de los productos y sus precios.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Se imprime el menú original con la palabra "Before:" antes de su contenido.
print("Before:", menu)

# Se agrega un nuevo elemento al diccionario 'menu' con la clave 'cheesecake' y el valor 8.
menu["cheesecake"] = 8

# Se imprime nuevamente el menú después de agregar el nuevo elemento.
print("After:", menu)

# Se actualiza el valor de la clave 'oatmeal' cambiando su precio de 3 a 5.
menu["oatmeal"] = 5

# Se imprime el menú mostrando el cambio en el precio de 'oatmeal'.
print("Oatmeal updated:", menu)

# Se crea un diccionario llamado 'oscar_winners' con categorías de los premios Oscar y sus ganadores.
oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

# Se imprime el contenido original del diccionario de ganadores.
print("Before:", oscar_winners)

# Se agrega una nueva categoría 'Supporting Actress' con su respectiva ganadora.
oscar_winners.update({"Supporting Actress": "Viola Davis"})

# Se modifica el valor de la clave 'Best Picture' para actualizar el ganador correcto.
oscar_winners["Best Picture"] = "Moonlight"

# Se imprime el diccionario después de las modificaciones.
print("Updated Oscars:", oscar_winners)

# Se crean dos listas: 'names' con nombres de estudiantes y 'heights' con sus alturas en pulgadas.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# Se combinan las dos listas en pares (nombre, altura) usando la función zip() dentro de una comprensión de diccionario.
# Cada nombre será una clave y su altura el valor correspondiente.
students = {name: height for name, height in zip(names, heights)}

# Se imprime el nuevo diccionario 'students' con los nombres y alturas de los estudiantes.
print(students)

# Se crea una lista llamada 'drinks' con diferentes tipos de bebidas.
drinks = ["espresso", "chai", "decaf", "drip"]

# Lista 'caffeine' que contiene la cantidad de cafeína correspondiente a cada bebida.
caffeine = [64, 40, 0, 120]

# Se combinan ambas listas usando zip() para crear un diccionario 'drinks_to_caffeine',
# donde la clave es la bebida y el valor es la cantidad de cafeína.
drinks_to_caffeine = {drink: mg for drink, mg in zip(drinks, caffeine)}

# Se imprime el diccionario resultante con las bebidas y su contenido de cafeína.
print(drinks_to_caffeine)

# Se crea una lista 'songs' con nombres de canciones.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]

# Lista 'playcounts' que contiene el número de reproducciones de cada canción en el mismo orden.
playcounts = [78, 29, 44, 21, 89, 5]

# Se combinan ambas listas con zip() dentro de una comprensión de diccionario para crear 'plays',
# donde la clave es el nombre de la canción y el valor el número de reproducciones.
plays = {song: count for song, count in zip(songs, playcounts)}

# Se imprime el diccionario 'plays' con las canciones y su número de reproducciones.
print(plays)

# Se agrega una nueva canción ('Purple Haze') al diccionario 'plays' con una reproducción inicial de 1.
plays.update({"Purple Haze": 1})

# Se actualiza el número de reproducciones de la canción 'Respect' a 94.
plays.update({"Respect": 94})

# Se imprime el diccionario 'plays' después de agregar y modificar elementos.
print("After:", plays)

# Se crea un diccionario 'library' que contiene otros diccionarios como valores (diccionarios anidados).
# La clave "The Best Songs" guarda el contenido del diccionario 'plays'.
# La clave "Sunday Feelings" se deja vacía para agregar canciones más adelante.
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

# Se imprime el contenido del diccionario 'library' mostrando su estructura interna.
print(library)
