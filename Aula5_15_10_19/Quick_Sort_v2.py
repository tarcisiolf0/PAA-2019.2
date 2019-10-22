def partition(array, low, high):
    pivot = array[high]
    bottom = low - 1

    top = low
    for top in range(high):
        if array[top] <= pivot:
            bottom += 1
            aux = array[bottom]
            array[bottom] = array[top]
            array[top] = aux

    aux = 0
    aux = array[bottom + 1]
    array[bottom + 1] = array[high]
    array[high] = aux
    return (bottom + 1)

def quick_sort(array, low, high):
    if low < high:
        position = 0
        position = partition(array, low, high)

        quick_sort(array, low, position - 1)
        quick_sort(array, position + 1, high)

k = [20, 50, 10, 15, 60, 30, 80]

quick_sort(k, 0 , len(k)-1)
print(k)