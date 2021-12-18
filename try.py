# def dfs(graph, start, visited=None, parent=[], articulation_points=set()):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited, articulation_points)
#     return visited
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()     
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
 



# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}
# graph = {1: [2], 2: [1], 3: [4], 4: [3], 6: [7], 7: [6]}
graph={1: set([2, 5]), 2: set([3,4,1]), 3: set([2]), 4: set([2]), 5: set([1,6,7]), 6: set([5]), 7: set([5])}
print(graph)
print(dfs(graph, 1))