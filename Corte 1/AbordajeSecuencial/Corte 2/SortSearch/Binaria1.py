def firstOccurrence(arr, n, key):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            high = mid - 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def lastOccurrence(arr, n, key):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def main():
    arr = [2, 7, 11, 14, 18, 19, 19, 21, 23, 45] #Se le debe dar el arreglo ordenado19
    
    n = len(arr)

    print("Arreglo (ordenado): ", end="")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    key = int(input("Ingrese el numero a buscar: "))

    first = firstOccurrence(arr, n, key)
    last = lastOccurrence(arr, n, key)

    if first == -1:
        print(f"El numero {key} NO se encuentra en el arreglo.")
    else:
        count = last - first + 1

        print(f"El numero {key} aparece {count} veces.")
        print("Posiciones (indices 0-based): ", end="")

        for i in range(first, last + 1):
            print(i, end=" ")
        print()


if __name__ == "__main__":
    main()
