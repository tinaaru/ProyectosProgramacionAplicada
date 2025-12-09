def linearSearch(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


def linearSearchAll(arr, n, key, indices):
    count = 0

    for i in range(n):
        if arr[i] == key:
            indices[count] = i
            count += 1

    return count


def main():
    arr = [41, 19, 12, 8, 3, 7, 9, 7]
    n = len(arr)

    print("Arreglo: ", end="")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    key = int(input("Ingrese el numero a buscar: "))

    pos = linearSearch(arr, n, key)

    if pos == -1:
        print(f"El numero {key} NO se encuentra en el arreglo.")
    else:
        print(f"El numero {key} se encuentra (al menos) en la posicion {pos} (indice 0-based).")

    indices = [0] * 100
    count = linearSearchAll(arr, n, key, indices)

    if count == 0:
        print(f"No se encontraron ocurrencias de {key}.")
    else:
        print(f"El numero {key} aparece {count} veces, en las posiciones: ", end="")
        for i in range(count):
            print(indices[i], end=" ")
        print()


if __name__ == "__main__":
    main()
