from collections import defaultdict
def reading_graph(path_to_file, type):
    """
    :param path_to_file:
    :param type: if type == 0, graph is oriented, if type == 1, graph is not oriented
    :return:
    """
    pre_final_set = set()
    final_set = set()
    with open(path_to_file, 'r') as file:
        first = True
        for line in file:
            line = line.strip()
            if first:
                pre_final_set.add((int(line.split(" ")[0]), int(line.split(" ")[1])))
                first = False
            else:
                one_line = (int(line.split(" ")[0]), int(line.split(" ")[1]))
                final_set.add(one_line)
    #print(pre_final_set)
    # return list(pre_final_set), final_set
    return list(pre_final_set), final_set

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


g = defaultdict(set)
add_edge(g, 0, 1)
add_edge(g, 1, 2)
add_edge(g, 2, 4)
add_edge(g, 2, 3)
add_edge(g, 3, 0)
add_edge(g, 4, 5)
add_edge(g, 5, 6)
add_edge(g, 6, 7)
add_edge(g, 6, 4)

#print(g)
#print("Strongly Connected Components:")
#print(kosaraju_scc(g, 8))

# data = reading_graph('graph_100_1942_0.csv', 1)
# n = data[0][0][1]

# for i in data[1]:
#     add_edge(g, i[0], i[1])

print(kosaraju_scc(g, 8))