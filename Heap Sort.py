


def heapify(arr, n, j):

    largest = j
    l = 2 * j + 1
    m = 2 * j + 2

    if l < n and arr[j] < arr[l]:
        largest = l

    if m < n and arr[largest] < arr[m]:
        largest = m


    if largest != j:
        arr[j], arr[largest] = arr[largest], arr[j]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)


    for j in range(n // 2, -1, -1):
        heapify(arr, n, j)

    for j in range(n - 1, 0, -1):

        arr[j], arr[0] = arr[0], arr[j]


        heapify(arr, j, 0)


arr = [2, 12, 8, 7, 4, 1]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for j in range(n):
    print("%d " % arr[j], end='')



