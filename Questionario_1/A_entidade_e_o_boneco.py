def lowest_value_remove(graph, array_times, source):
    time_aux = 0
    global total_time, remove_node, latest_time, latest_removed_node
    print("Vertex {} ".format(source))
    if removed[source] == 0:
        for v in graph[source]:
            print("Adj_List {} | Vertexs {}".format(graph[source], v))
            if removed[v] == 0:
                time_aux += array_times[v]

        if (time_aux <= latest_time):
            print("time_aux {} | latest_time {} | time_array_source {} | time_array_latest_removed {} | source {} | latest_node {}".
                  format(time_aux, latest_time, array_times[source], array_times[latest_removed_node], source, latest_removed_node))
            if time_aux == latest_time and array_times[source] > array_times[latest_removed_node]:
                print("TEMPO IGUAL")
                latest_removed_node = source
                latest_time = time_aux
                remove_node = source
            else:
                latest_removed_node = source
                latest_time = time_aux
                remove_node = source
        print(
            "time_aux {} | latest_time {} | time_array_source {} | time_array_latest_removed {} | source {} | latest_node {}".
            format(time_aux, latest_time, array_times[source], array_times[latest_removed_node], source,
                   latest_removed_node))

        print(source, time_aux)
        pieces_times[source] = time_aux


# Graph
def empty_list(list, size):
    for i in range(size):
        list.append( [] )

def init_undirected_graph(graph, vertex_1, vertex_2):
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)


# Input
pieces, strings = input().split(" ")
pieces = int(pieces)
strings = int(strings)
array_times = input().split(" ")
array_times = [int(num) for num in array_times]

array_times = [-1] + array_times

graph = []
empty_list(graph, pieces + 1)

for i in range(strings):
    aux = input().split(" ")
    aux = [int(num) for num in aux]
    vertex_1, vertex_2 = aux
    init_undirected_graph(graph, vertex_1, vertex_2)



# Functions
pieces_times = []
removed = []
total_time = 0
remove_node = -1
nodes_removed = 0
latest_time = 10000000

latest_removed_node = -1

# Inicializando os arrays auxiliares
for k in range(pieces + 1):
    pieces_times.append(1000000)
    removed.append(0)


print(graph)


while(nodes_removed < pieces):
    latest_time = 1000000
    latest_removed_node = -1
    for l in range(1, len(graph)):
        lowest_value_remove(graph, array_times, l)

    total_time += pieces_times[remove_node]
    print("Tempo Remoção {} | Nó Removido {}".format(total_time, remove_node))
    removed[remove_node] = 1
    print("Array de removidos", removed)
    pieces_times[remove_node] = 1000000
    print("Tempo das peças após remoção", pieces_times)
    nodes_removed += 1
    print("\n")

print("\n\n")
print(removed)
print(pieces_times)
print(graph)
print(array_times)
