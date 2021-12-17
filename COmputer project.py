def read_file(file_path):
    graph=[(1,2),(1,3),(2,11),(2,4),(3,11),(11,4),(11,5),(4,5),(5,9),(5,8),(5,7),(5,6),(6,7),(7,8),(8,9),(8,10),(9,10)]
    return graph
    pass


def write_file(file_path):
    pass


def component(graph):
    pass


def strongly_connected_component(graph):
    pass


def connection_points(graph):
    points=[]
    graph_component=component(graph)
    for i in graph:

        graphnew=graph.remove(i)
        if component(graphnew)!=graph_component:
            points.append(i)
    return points


def bridge(graph):
    pass


print(connection_points(read_file(1)))