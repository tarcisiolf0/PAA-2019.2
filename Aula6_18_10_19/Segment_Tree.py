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


# leitura de dados
n = int(input()) + 1
array = list(map(int, input().split()))
array = [0] + array
b, e = map(int, input().split())

# altura da arvore (coloco mais 1 para gerar sempre uma arvore completa)
h = int(log(float(n), 2)) + 1 
# numero maximo de nos (mantive um a mais para ignorar a posição 0), 
storage = [0] * ((2 ** h) * 2 + 1)

build(1, 1, n)
print(sum(b,e,1, 1, n))
modify(2, 7, 1, 1, n)
print(sum(b,e,1, 1, n))