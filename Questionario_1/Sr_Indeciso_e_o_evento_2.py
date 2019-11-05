# Segment Tree
from math import *
storage = []
array = []

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
    if node_e - node_b < 2:
        array[position] = value
    else:
        mid = int((node_b + node_e) / 2)
        if position < mid:
            modify(position, value, index * 2, node_b, mid)
        else:
            modify(position, value, (index * 2) + 1, mid, node_e)

# End
size = int(input())

aux = input().split(" ")
money = [int(num) for num in aux]

cases = int(input())
print(size, money, cases)
for j in range(cases):
    aux2 = list()
    aux = input().split(" ")
    requisition = aux[0]
    parameter1 = int(aux[1])
    parameter2 = int(aux[2])
    aux2.append(requisition)
    aux2.append(parameter1)
    aux2.append(parameter2)


#    if aux2[0] == "Q":
#        function

#    elif aux2[0] == "U":
#        function