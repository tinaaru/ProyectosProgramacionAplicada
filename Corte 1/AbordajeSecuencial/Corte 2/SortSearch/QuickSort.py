def swap(a, b):
    return b, a

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = swap(arr[i], arr[j])

    arr[i + 1], arr[high] = swap(arr[i + 1], arr[high])
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()

def main():
    arr = [10, 3, 8, 0, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr, n)

    quickSort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    printArray(arr, n)

if __name__ == "__main__":
    main()
