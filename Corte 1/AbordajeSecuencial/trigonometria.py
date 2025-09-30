import math

# Solicitar al usuario un ángulo en radianes
radianes = float(input("Ingrese un valor en radianes: "))

# Calcular el seno directamente en radianes
proyeccion_rad = math.sin(radianes)
print("Seno en radianes:", proyeccion_rad)

# Convertir de radianes a grados
grados = math.degrees(radianes)  # Más claro que multiplicar por (180/pi)
print("Conversión de radianes a grados:", grados)

# Si quiero calcular el seno a partir de un valor en grados,
# debo convertir los grados de nuevo a radianes antes de usar math.sin
proyeccion_deg = math.sin(math.radians(grados))
print("Seno en grados (convertido a radianes):", proyeccion_deg)
