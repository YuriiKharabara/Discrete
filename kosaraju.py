from collections import defaultdict

def add_edge(graph, s, d):
    graph[s].append(d)
    # dfs

def dfs(graph, d, visited_vertex):
    visited_vertex[d] = True
    print(d, end='')
    for i in graph[d]:
        if not visited_vertex[i]:
            dfs(graph, i, visited_vertex)

def fill_order(graph, d, visited_vertex, stack):
    visited_vertex[d] = True
    for i in graph[d]:
        if not visited_vertex[i]:
            fill_order(graph, i, visited_vertex, stack)
    stack = stack.append(d)

    # transpose the matrix
def transpose(graph):
    g = defaultdict(list)

    for i in graph:
        for j in graph[i]:
            add_edge(g, j, i)
    return g

    # Print stongly connected components
def print_scc(graph, vert_counter):
    stack = []
    visited_vertex = [False] * vert_counter

    for i in range(len(graph)):
        if not visited_vertex[i]:
            fill_order(graph, i, visited_vertex, stack)

    gr = transpose(graph)

    visited_vertex = [False] * vert_counter

    while stack:
        i = stack.pop()
        if not visited_vertex[i]:
            dfs(gr, i, visited_vertex)
            print("")

g = defaultdict(list)
add_edge(g, 0, 1)
add_edge(g, 1, 2)
add_edge(g, 2, 3)
add_edge(g, 2, 4)
add_edge(g, 3, 0)
add_edge(g, 4, 5)
add_edge(g, 5, 6)
add_edge(g, 6, 4)
add_edge(g, 6, 7)

print("Strongly Connected Components:")
print_scc(g, 8)