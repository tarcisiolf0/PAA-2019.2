graph = []
visited = []
colors = []

# 0 = white; 1 = black
def floodfill(u, color):
    global visited, graph
    print(u)

    visited[u] = True
    colors[u] = color
    for v in graph[u]:
        if colors[v] == "white":
            floodfill(v, color)

# Ilustra a criação de um grafo direcionado
def init_directed_graph():
    global visited, graph, colors

    vertices = 4
    visited = [False] * vertices
    # Lista de adjacências para cada vértice
    for i in range(0, vertices):
        graph.append([])
        colors.append("white")

    graph[0].append(1)  # 0 -> 1
    graph[0].append(2)  # 0 -> 2
    graph[1].append(2)  # 1 -> 2
    graph[2].append(3)  # 2 -> 3

    print(graph)

    floodfill(0, "black")

init_directed_graph()
print(colors)
print(visited)