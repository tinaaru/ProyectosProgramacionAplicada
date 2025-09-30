# Programa para determinar si un número es par o impar

while True:
    try:
        # Pedir al usuario un número
        entrada = input("Digite el número que desea consultar (o 'q' para salir): ")

        # Opción para terminar el programa
        if entrada.lower() == 'q':
            print("Programa finalizado.")
            break

        # Intentar convertir la entrada a entero
        num = int(entrada)

        # Verificar si el número es par o impar
        if num % 2 == 0:
            print(f"{num} es PAR")
        else:
            print(f"{num} es IMPAR")

    except ValueError:
        # En caso de que el usuario no escriba un número válido
        print("⚠️ Error: Ingrese un número válido.")
