def dfs(graph, start, visited=None, parent=[], articulation_points=set()):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited, articulation_points)
    return visited


def dfs_iterative(graph, start):
    stack=[start]
    stack= [start]
    path=[]

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path




graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
dfs(graph, '0')
print(dfs_iterative(graph, '0'))