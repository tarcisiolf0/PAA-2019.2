# Segment Tree
from math import *
storage = []
array = []
min_seg_tree = []

# index = indice da seg_tree (inicialmente = 1)
# left = intervalo esquerdo fechado do array
# right = intervalo direito aberto do array


def build(index, left, right):
    if right - left < 2:
        storage[index] = array[left]
        return
    mid = int((left + right) / 2)
    build(index * 2, left, mid)
    build((index * 2) + 1, mid, right)
    storage[index] = storage[index * 2] + storage[(index * 2) + 1]


def sum(begin, end, index, node_b, node_e):
    if begin >= node_e or end <= node_b:
        return 0
    elif begin <= node_b and end >= node_e:
        return storage[index]
    else:
        mid = int((node_b + node_e) / 2)
        return sum(begin, end, index * 2, node_b, mid) + sum(begin, end, (index * 2) + 1, mid, node_e)


def modify(position, value, index, node_b, node_e):
    storage[index] += (value - array[position])
    min_seg_tree[index] += (value - array[position])
    if node_e - node_b < 2:
        array[position] = value
    else:
        mid = int((node_b + node_e) / 2)
        if position < mid:
            modify(position, value, index * 2, node_b, mid)
        else:
            modify(position, value, (index * 2) + 1, mid, node_e)


def construct_min_seg_tree(index, left, right):
    if right - left < 2:
        min_seg_tree[index] = array[left]
        return

    mid = int((left + right) / 2)

    construct_min_seg_tree(index * 2, left, mid)
    construct_min_seg_tree((index * 2) + 1, mid, right)

    min_seg_tree[index] = min(min_seg_tree[(2 * index)], min_seg_tree[(2 * index) + 1])


def min_range(begin, end, node_b, node_e, index):
    if begin <= node_b and end >= node_e:
        return min_seg_tree[index]
    elif begin > node_e or end < node_b:
        return 1000000

    mid = int((node_b + node_e) / 2)
    aux1 = min_range(begin, end, node_b, mid, (2 * index))
    aux2 = min_range(begin, end, mid + 1, node_e, (2 * index) + 1)
    return min(aux1, aux2)


# Teste
size = int(input())

aux = input().split(" ")
array = [int(num) for num in aux]

cases = int(input())

# Construindo a segment tree
n = size + 1
array = [0] + array

# altura da arvore (coloco mais 1 para gerar sempre uma arvore completa)
h = int(log(float(n), 2)) + 1

# numero maximo de nos (mantive um a mais para ignorar a posição 0),
storage = [0] * ((2 ** h) * 2 + 1)
build(1, 1, n)

min_seg_tree = [1000000] * ((2 ** h) * 2 + 1)
construct_min_seg_tree(1, 1, n)

# Obs: quando chamar a função sum tem que somar 1 no primeiro parâmetro e 2 no segundo
for j in range(cases):
    aux2 = list()
    aux = input().split(" ")
    requisition = aux[0]
    parameter1 = int(aux[1])
    parameter2 = int(aux[2])
    aux2.append(requisition)
    aux2.append(parameter1)
    aux2.append(parameter2)

    if requisition == "Q":
        result_sum = sum(parameter1 + 1, parameter2 + 2, 1, 1, n)
        result_min = min_range(parameter1 + 1, parameter2 + 2, 1, n, 1)
        print(result_sum, result_min)

    elif requisition == "U":
        modify(parameter1+1, parameter2, 1, 1, n)
