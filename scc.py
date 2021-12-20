from collections import defaultdict


def add_edge(graph, s, d):
    graph[s].add(d)
    # dfs


def dfs(graph, d, visited_vertex):
    curr = []
    visited_vertex[d] = True
    #print(d, end='')
    curr.append(d)
    for i in graph[d]:
        if not visited_vertex[i]:
            dfs(graph, i, visited_vertex)
    return curr


def fill_order(graph, d, visited_vertex, stack):
    visited_vertex[d] = True
    for i in graph[d]:
        if not visited_vertex[i]:
            fill_order(graph, i, visited_vertex, stack)
    stack = stack.append(d)

    # transpose the matrix


def transpose(graph):
    g = defaultdict(set)

    for i in graph:
        for j in graph[i]:
            add_edge(g, j, i)
    return g

    # Print stongly connected components


def kosaraju_scc(graph, vert_counter):
    scc = []
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
            scc += dfs(gr, i, visited_vertex)
    return scc


# print(g)
#print("Strongly Connected Components:")
# print(kosaraju_scc(g, 8))
