import random

def quick_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    left = right = pivot = 0
    left = left_index
    right = right_index
    pivot = array[(left_index + right_index) // 2]

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right += -1

        if left <= right:
            aux = array[left]
            array[left] = array[right]
            array[right] = aux
            left += 1
            right += -1

        quick_sort(array, left_index, right)
        quick_sort(array, left, right_index)

# Teste

array = list()
for i in range(5):
    array.append(random.randrange(50))

print(array)
quick_sort(array, 0, len(array)-1)
print("Array ordenado", array)