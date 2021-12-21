def dfs(at, graph, stack, on_stack, ids, low, ident, comps):
    on_stack[at] = True
    ids[at] = low[at] = ident 
    ident += 1
    stack.append(at)
    for to in graph[at]:
        if ids[to] == -1:
            dfs(to, graph, stack, on_stack, ids, low, ident, comps)
            low[at] = min(low[at], low[to])
        elif on_stack[to]:
            low[at] = min(low[at], low[to])
    w = None
    if ids[at] == low[at]:
        curr = []
        while w != at:
            w = stack.pop()
            curr.append(w)
            on_stack[w] = False
            low[w] = ids[at]
        comps.append(min(curr))

def tarjan_scc(n, graph):
    '''
    Finds strongly connected components in graph
    >>> tarjan_scc(9, [[], [2], [3], [1], [5, 8], [6], [1, 7], [1, 5, 3], [4, 6]])
    [1, 5, 4]
    '''
    # try:
    ids = [-1] * n
    low = [-1] * n
    on_stack = [False] * n
    stack = []
    ident = 0
    comps = []

    for i in range(n):
        if ids[i] == -1:
            dfs(i, graph, stack, on_stack, ids, low, ident, comps)
    comps.remove(0)
    return comps
    # except:
    #     return 'incorrect input data'

# graph = [[1], [2], [0], [4, 7], [5], [0, 6], [0, 4, 2], [3, 5]]
# n = 8
# print(tarjan_scc(n, graph))
# import doctest
# doctest.testmod()