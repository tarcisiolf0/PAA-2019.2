lowest_left = 1000000
larger_right = -1


def find_x(array, left, right, x):
    if left == right:
        if x == array[left]:
            return left
        else:
            print(left, left - 1)
            return -1

    mid = (left + right) // 2

    if array[mid] == x:
        # Modificado
        global lowest_left
        global larger_right

        # Ao achar o numero desejado, verifica se encontra um indice menor
        if mid <= lowest_left:
            lowest_left = mid
            if array[mid - 1] == x:
                lowest_left = mid - 1
                find_x(array, left, mid, x)

        # Ao achar o numero desejado, verifica se encontra um indice maior
        if mid >= larger_right:
            larger_right = mid
            if array[mid + 1] == x:
                larger_right = mid + 1
                find_x(array, mid + 1, right, x)
        # Até aqui

        return mid

    elif x < array[mid]:
        return find_x(array, left, mid, x)
    else:
        return find_x(array, mid + 1, right, x)


size = int(input())

aux = input().split(" ")
money = [int(num) for num in aux]

cases = int(input())
for j in range(cases):
    aux = int(input())
    result = find_x(money, 0, size - 1, aux)
    if lowest_left != 100000 and larger_right != -1:
        print(lowest_left, larger_right)

    # Caso onde o numero desejado e o ultimo do array
    if result == size - 1:
        print(size - 1, size - 1)

    lowest_left = 1000000
    larger_right = -1
