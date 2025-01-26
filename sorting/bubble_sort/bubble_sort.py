# big O -> (n (n + 1)) / 2 -> n**2 + n -> n**2

def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                aux = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = aux

    return arr