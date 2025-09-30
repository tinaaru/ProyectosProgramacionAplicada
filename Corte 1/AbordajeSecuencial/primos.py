# Programa para verificar números primos hasta un valor dado por el usuario

while True:
    num = input("Ingrese un número (o 'q' para salir): ")

    # Opción para salir del programa
    if num.lower() == 'q':
        print("Programa finalizado.")
        break

    # Validar que la entrada sea un número entero
    try:
        num = int(num)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  # vuelve a pedir el número

    # Recorremos desde 1 hasta el número ingresado
    for i in range(1, num + 1):
        conta = 0  # contador de divisores

        # Verificar divisores de i
        for n in range(1, int(i ** 0.5) + 1):  # optimización: solo hasta raíz de i
            if i % n == 0:
                conta += 1
                if n != i // n:  # evitar contar el mismo divisor dos veces
                    conta += 1

        # Un número primo tiene exactamente 2 divisores (1 y él mismo)
        if conta == 2:
            print(f"{i} → Sí es un número primo")
        else:
            print(f"{i} → No es un número primo")
