#### Get A Key #OBTENER UNA CLAVE
# Puedes acceder a los valores de un diccionario proporcionando la clave.

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  
# Crea un nuevo diccionario llamado building_heights con claves (nombres de edificios) y valores (alturas en metros).

print(building_heights["Burj Khalifa"])  
# Imprime el valor correspondiente a la clave "Burj Khalifa" dentro del diccionario (828).

print(building_heights["Ping An"])  
# Imprime el valor correspondiente a la clave "Ping An" dentro del diccionario (599).


zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}
# Crea un nuevo diccionario llamado zodiac_elements, donde cada clave representa un elemento y su valor es una lista de signos zodiacales asociados.

print(zodiac_elements["earth"])  
# Imprime el valor (lista) correspondiente a la clave "earth" (["Taurus", "Virgo", "Capricorn"]).

print(zodiac_elements["fire"])  
# Imprime el valor (lista) correspondiente a la clave "fire" (["Aries", "Leo", "Sagittarius"]).


## Get an Invalid Key #OBTENER UNA CLAVE NO VÁLIDA

building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}
# Crea nuevamente el diccionario building_heights.

print(building_heights["Landmark 81"])
# Intenta imprimir el valor de la clave "Landmark 81", pero como no existe, Python lanzará un error (KeyError).


## Una forma de evitar este error es verificar primero si la clave existe en el diccionario.

key_to_check = "Landmark 81"
# Guarda la clave a verificar en la variable key_to_check.

if key_to_check in building_heights:
    # Comprueba si la clave "Landmark 81" se encuentra dentro del diccionario building_heights.
    print(building_heights["Landmark 81"])
    # Si existe, imprime el valor asociado a esa clave.


zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}
# Crea nuevamente el diccionario zodiac_elements.

zodiac_elements["energy"] = "Not a Zodiac element"
# Agrega una nueva clave "energy" con el valor "Not a Zodiac element" al diccionario zodiac_elements.

if "energy" in zodiac_elements:
    # Comprueba si la clave "energy" existe dentro del diccionario.
    print(zodiac_elements["energy"])
    # Si existe, imprime el valor asociado ("Not a Zodiac element").


## Safely Get a Key #OBTENER UNA CLAVE DE FORMA SEGURA

building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}
# Crea el diccionario building_heights nuevamente.

building_heights.get("Shanghai Tower")
# Devuelve el valor de la clave "Shanghai Tower" (632).  
# Si la clave no existiera, no generaría error, sino que devolvería None.

building_heights.get("My House")
# Intenta obtener la clave "My House", pero como no existe, devuelve None sin error.


user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}
# Crea un diccionario llamado user_ids con nombres de usuario como claves y números como valores.

user_ids.get("teraCoder")
# Devuelve el valor 100019 asociado a la clave "teraCoder".


if user_ids.get("teraCoder") == None:
    # Comprueba si la clave "teraCoder" no existe (sería None).
    tc_id = 1000
    # Si no existe, asigna 1000 a la variable tc_id.
else:
    tc_id = user_ids.get("teraCoder")
    # Si sí existe, asigna el valor obtenido (100019) a tc_id.

print(tc_id)
# Imprime el valor de tc_id (100019 en este caso).

if user_ids.get("superStackSmash") == None:
    # Comprueba si la clave "superStackSmash" no existe.
    stack_id = 100000
    # Si no existe, asigna 100000 a la variable stack_id.

print(stack_id)
# Imprime el valor de stack_id (100000).


### Delete a Key #BORRAR UNA CLAVE
# El método .pop() sirve para eliminar un elemento del diccionario conociendo su clave, y devuelve su valor.

raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker"
}
# Crea un diccionario llamado raffle con números como claves y premios como valores.

print(raffle.pop(320291, "No Prize"))
# Elimina la clave 320291 del diccionario y devuelve su valor ("Gift Basket").  
# Si no existiera la clave, imprimiría "No Prize".

print(raffle)
# Imprime el diccionario actualizado sin la clave eliminada (320291).

print(raffle.pop(100000, "No Prize"))
# Intenta eliminar la clave 100000, pero como no existe, devuelve "No Prize".

print(raffle)
# Imprime el diccionario sin cambios.

print(raffle.pop(872921, "No Prize"))
# Elimina la clave 872921 y devuelve su valor ("Concert Tickets").

print(raffle)
# Imprime el diccionario actualizado sin la clave 872921.


available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}
# Crea un diccionario llamado available_items con objetos y sus valores numéricos.

health_points = 20
# Crea una variable health_points con valor inicial 20.

health_points += available_items.pop("stamina grains", 0)
# Suma a health_points el valor de la clave "stamina grains" (15) y elimina la clave del diccionario.  
# Si no existiera, sumaría 0.

health_points += available_items.pop("power stew", 0)
# Suma a health_points el valor de la clave "power stew" (30) y elimina la clave.  
# Si no existiera, sumaría 0.

health_points += available_items.pop("mystic bread", 0)
# Intenta eliminar la clave "mystic bread". Como no existe, suma 0.

print(available_items)
# Imprime el nuevo diccionario sin las claves eliminadas ("stamina grains" y "power stew").

print(health_points)
# Imprime el valor total acumulado de health_points (20 + 15 + 30 = 65).


## Get All Keys #OBTENER TODAS LAS CLAVES

test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}
# Crea un diccionario llamado test_scores con estudiantes y sus listas de puntajes.

print(list(test_scores))
# Imprime una lista con todas las claves del diccionario (nombres de estudiantes).

for student in test_scores.keys():
    # Recorre todas las claves (nombres de estudiantes) del diccionario test_scores.
    print(student)
    # Imprime cada nombre uno por uno.


user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}
# Crea nuevamente el diccionario user_ids.

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}
# Crea un diccionario num_exercises con el número de ejercicios por tema.

users = user_ids.keys()
# Obtiene una vista de todas las claves (usuarios) del diccionario user_ids.

lessons = num_exercises.keys()
# Obtiene una vista de todas las claves (lecciones) del diccionario num_exercises.

print(users)
# Imprime la vista de claves del diccionario user_ids.

print(lessons)
# Imprime la vista de claves del diccionario num_exercises.


## Get All Values #OBTENER TODOS LOS VALORES

test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}
# Crea nuevamente el diccionario test_scores.

for score_list in test_scores.values():
    # Recorre todos los valores (listas de puntajes) del diccionario test_scores.
    print(score_list)
    # Imprime cada lista de puntajes una por una.


num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}
# Crea nuevamente el diccionario num_exercises.

total_exercises = 0
# Crea una variable total_exercises e inicialízala en 0.

for exercises in num_exercises.values():
    # Recorre todos los valores del diccionario (número de ejercicios por tema).
    total_exercises += exercises
    # Suma cada valor al total acumulado.

print(total_exercises)
# Imprime el total de ejercicios sumados (10+13+15+22+19+18+18 = 115).


## Get All Items #OBTENER TODOS LOS PARES CLAVE-VALOR

biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}
# Crea un diccionario llamado biggest_brands con marcas y sus valores en miles de millones.

for company, value in biggest_brands.items():
    # Recorre el diccionario obteniendo cada par clave-valor (empresa y valor).
    print(company + " has a value of " + str(value) + " billion dollars.")
    # Imprime un mensaje combinando el nombre de la empresa y su valor.


pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}
# Crea un diccionario llamado pct_women_in_occupation con profesiones y porcentaje de mujeres en ellas.

for occupation, percentage in pct_women_in_occupation.items():
    # Recorre todos los pares clave-valor del diccionario.
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
    # Imprime una frase indicando el porcentaje de mujeres en cada ocupación.
