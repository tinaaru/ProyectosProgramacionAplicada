def insertionSort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    arr = [3, 2, 0, 6, 1]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr, n)

    insertionSort(arr, n)

    print("Arreglo ordenado:")
    printArray(arr, n)

if __name__ == "__main__":
    main()
