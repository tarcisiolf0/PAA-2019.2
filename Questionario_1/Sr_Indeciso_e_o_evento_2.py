# Segment Tree
from math import *
storage = []
array = []
min_seg_tree = []

# index = indice da seg_tree (inicialmente = 1)
# left = intervalo esquerdo fechado do array
# right = intervalo direito aberto do array


def build(index, left, right):
    if left == right:
        storage[index] = array[left]
        min_seg_tree[index] = array[left]
        return
    mid = (left + right) // 2
    build(index * 2, left, mid)
    build((index * 2) + 1, mid + 1, right)
    storage[index] = storage[index * 2] + storage[(index * 2) + 1]
    min_seg_tree[index] = min(min_seg_tree[(2 * index)], min_seg_tree[(2 * index) + 1])

def getSum(begin, end, index, node_b, node_e):
    if node_e < begin or node_b > end:
        return 0
    elif begin <= node_b and end >= node_e:
        return storage[index]
    else:
        mid = (node_b + node_e) // 2
        return getSum(begin, end, index * 2, node_b, mid) + getSum(begin, end, (index * 2) + 1, mid + 1, node_e)

def min_range(begin, end, node_b, node_e, index):
# Se o intervalo procurado faz parte do intevalo dado
    if begin <= node_b and end >= node_e:
        return min_seg_tree[index]
# Se o intervalo procurado esta fora do intevalo dado
    elif node_e < begin or node_b > end:
        return 1000001
# Se parte dessa segment_tree sobrep?e o intervalo dado
    mid = (node_b + node_e) // 2
    aux1 = min_range(begin, end, node_b, mid, (2 * index))
    aux2 = min_range(begin, end, mid+1, node_e, (2 * index) + 1)
    return min(aux1, aux2)

def modify(position, value, index, node_b, node_e):
    if node_b == node_e:
        storage[index] += (value - array[position])
        min_seg_tree[index] = value
        array[position] = value
    else:
        mid = (node_b + node_e) // 2
        if position <= mid:
            modify(position, value, index * 2, node_b, mid)
        else:
            modify(position, value, (index * 2) + 1, mid + 1, node_e)
        storage[index] = storage[2*index] + storage[2*index + 1]
        min_seg_tree[index] = min(min_seg_tree[2*index], min_seg_tree[2*index + 1])


# Teste
size = int(input())

aux = input().split()
array = [int(num) for num in aux]

cases = int(input())

# Construindo a segment tree
n = size
array = [0] + array

# altura da arvore (coloco mais 1 para gerar sempre uma arvore completa)
h = int(log(float(n+1), 2)) + 1

# numero maximo de nos (mantive um a mais para ignorar a posi??o 0),
storage = [0] * ((2 ** h) * 2 + 1)
min_seg_tree = [1000001] * ((2 ** h) * 2 + 1)
build(1, 1, n)

# Obs: quando chamar a fun??o sum tem que somar 1 no primeiro par?metro e 2 no segundo
for j in range(cases):
    aux = input().split()
    requisition = aux[0]
    parameter1 = int(aux[1])
    parameter2 = int(aux[2])

    if requisition == "Q":
        result_sum = getSum(parameter1 + 1, parameter2 + 1, 1, 1, n)
        result_min = min_range(parameter1 + 1, parameter2 + 1, 1, n, 1)
        print(result_sum, result_min)

    elif requisition == "U":
        modify(parameter1 + 1, parameter2, 1, 1, n)
