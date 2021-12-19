def read_graph(path_to_file, type):
    pass

def write_file(file_path):
    pass


def component(graph):
    pass


def strongly_connected_component(graph):
    pass

def dfs(graph, start, d=[], h=[], ch=0, visited=None, p=-1, root=0, articulation_poins=set()):
    if visited is None:
        visited = set()
        root=start
    visited.add(start)
    if p != -1:
        h[start] = h[p] + 1
        d[start] = h[start]
    else:
        h[start]=d[start]=0
    for next in set(graph[start]) & visited:
        if next != p:
            d[start] = min(d[start], h[next])

    for next in set(graph[start]) - visited:
        dfs(graph, next, d, h, ch, visited, start, root, articulation_poins)
        d[start] = min(d[start], d[next])
        if h[start] <= d[next] and p != -1:
            articulation_poins.add(start)
    if p==-1 and len(graph[start])>1:
        articulation_poins.add(0)
        
    return articulation_poins