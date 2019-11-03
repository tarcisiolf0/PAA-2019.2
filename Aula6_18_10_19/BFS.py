from queue import *

def bfs(graph, vertex, source, ar):
    distance = []
    visited = []
    for x in range(0, vertex):
        distance.append(-1)
        visited.append(False)

    distance[ int(source) ] = 0
    visited[ int(source) ] = True
    q = Queue()
    q.put( source )
    while not q.empty():
        u = q.get()
        print( "Vértice " + str(u) + " com distância " + str(distance[int(u)]) )
        for w in graph[ int(u) ]:
            if not visited[ int(w) ]:
                distance[ int(w) ] = int(distance[int(u)]) + 1
                visited[ int(w) ] = True
                q.put(w)
    return visited[ int(ar) ]


def initGraphDirect():
    graph = [[]]
    v = 4
    for x in range(0,v-1):
        graph.append( [] )
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(2)
    graph[2].append(3)
    print(graph)
    bfs(graph,v,0,3)

def initGraphUndirected():
    graph = [[]]
    vertex = 4
    for x in range(0,vertex - 1):
        graph.append( [] )
    graph[0].append(1)
    graph[1].append(0)
    graph[0].append(2)
    graph[2].append(0)
    graph[1].append(2)
    graph[2].append(1)
    graph[2].append(3)
    graph[3].append(2)
    print(graph)
    bfs(graph,vertex,0,3)

initGraphDirect()

initGraphUndirected()
