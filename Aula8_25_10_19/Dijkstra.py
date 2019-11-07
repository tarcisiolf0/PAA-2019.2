from queue import *


def empty_list(list, size):
    for i in range(size):
        list.append([])


def graph_build(vertex_u, vertex_v, gain, graph):
    graph[vertex_u].append([vertex_v, gain])
    graph[vertex_v].append([vertex_u, gain])


def graph_print(list):
    for i in range(len(list)):
        print(list[i])


def dijsktra(graph, source):
    distance = []
    visited = []

    for i in range(len(graph)):
        distance.append(10 ** 5)
        visited.append(0)

    distance[source] = 0
    q = PriorityQueue()
    q.put([distance[source], source])

    while not q.empty():

        aux = q.get()
        vertex_1 = aux[1]
        if visited[vertex_1] == 0:
            visited[vertex_1] = 1
            for aux2 in graph[vertex_1]:
                vertex_2 = aux2[0]
                gain_2 = aux2[1]

                if (distance[vertex_1] + gain_2) < distance[vertex_2]:
                    distance[vertex_2] = distance[vertex_1] + gain_2
                    q.put([distance[vertex_2], vertex_2])

    return distance
