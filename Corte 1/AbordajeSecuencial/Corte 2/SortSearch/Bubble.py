def bubbleSort(arr, n):
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

def main():
    arr = [9, 1, 4, 0, 8]
    n = len(arr)
    print("Tamaño del arreglo:", n)

    print("Arreglo original:")
    printArray(arr, n)

    bubbleSort(arr, n)

    print("Arreglo ordenado:")
    printArray(arr, n)

if __name__ == "__main__":
    main()
