"Discrete project"

import scc
import copy
import numpy
import bridges


def read_graph(path_to_file, type, project):
    """
    :param path_to_file:
    :param type: if type == 0, graph is oriented, if type == 1, graph is not oriented 
    :return: set of tuples
    """
    try:
        three_2 = {}
        six = set()
        data = numpy.genfromtxt(path_to_file, delimiter=' ', skip_header=1)
        data[:, 0]
        for line in data:
            first = int(line[0])
            sec = int(line[1])
            if first in three_2.keys():
                three_2[first].add(sec)
            else:
                three_2[first] = set()
                three_2[first].add(sec)
            if int(type) == 0:
                if sec in three_2.keys():
                    continue
                else:
                    three_2[sec] = set()
            if int(type) == 1:
                if sec in three_2.keys():
                    three_2[sec].add(first)
                else:
                    three_2[sec] = set()
                    three_2[sec].add(first)
            six.add(tuple([first, sec]))
        if project == 3:
            return three_2
        elif project == 6:
            return six
        elif project == 5:
            five = [three_2[value] for value in sorted(three_2)]
            return five
    except OSError:
        return 'Такого шляху не існує'


def read_first_line(path_to_file):
    """
    This function reads only first line
    """
    with open(path_to_file) as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            break
    return (int(line[0]), int(line[1]))


def dfs(graph, start, visited=None):
    """Depth-first search funvtion
    >>> dfs({1: {2}, 2: {1}}, 1)
    {1, 2}
    """
    if visited is None:
        visited = set()
    visited.add(start)
    part1 = graph[start] - visited
    for next in part1:
        dfs(graph, next, visited)
    return visited


def connected_component(grahp_dict: dict):
    """
    Function to search connected component
    >>> connected_component({1: {2,3}, 2: {1, 3}, 3: {1, 3}, 4:{5}, 5: {4}})
    [1, 4]
    """
    keys = grahp_dict.keys()
    total_res = []
    visited = None
    counter = 0
    for i in keys:
        if counter == 0:
            visited = dfs(grahp_dict, i, visited)
            total_res.append(min(visited))

        elif i not in visited:
            old = copy.deepcopy(visited)
            visited = dfs(grahp_dict, i, visited)
            new = visited - old
            total_res.append(min(new))
        counter += 1
    return sorted(total_res)


def articulation_points(graph, start, d=[], h=[], ch=0, visited=None, p=-1, root=0, articulation_poins=set()):
    """
    Returns set of articulation points in graph
    >>> print(articulation_points([[2, 4, 5], [4, 5], [0, 3, 4], [6, 7, 2], [5, 2, 0], [0, 1, 4], [7, 8, 3], [3, 6, 8], [6, 7]], 0, [0]*8, [0]*8))
    [0, 2, 3]
    """
    try:
        if visited is None:
            visited = set()
            root = start
        visited.add(start)
        if p != -1:
            h[start] = h[p] + 1
            d[start] = h[start]
        else:
            h[start] = d[start] = 0
        for next in set(graph[start]) & visited:
            if next != p:
                d[start] = min(d[start], h[next])

        for next in set(graph[start]) - visited:
            articulation_points(graph, next, d, h, ch, visited,
                                start, root, articulation_poins)
            d[start] = min(d[start], d[next])
            if h[start] <= d[next] and p != -1:
                articulation_poins.add(start)
        if p == -1 and len(graph[start]) > 1:
            articulation_poins.add(0)
        articulation_poins = list(articulation_poins)
        return articulation_poins
    except IndexError:
        return 'У графі немає точок сполучення'


def main():
    path_to_file = input('    Введіть шлях до файлу:\n>>> ')
    while True:
        try:
            type_of_graph = int(input('''
    Виберіть тип графу:
    0 - якщо граф орієнтований
    1 - якщо граф неорієнтований\n>>> '''))
            if type_of_graph == 0:
                print("Список компонент сильної зв'язності:")
                graph = read_graph(path_to_file, 0, 5)
                graph.insert(0, [])
                print(scc.tarjan_scc(len(graph), graph))
            elif type_of_graph == 1:
                task_type = int(input('''
    Виберіть що ви бажаєте дізнатись про граф (введіть номер пункту):
    1 - список компонент зв'язності (граф неорієнтований);
    2 - список точок сполучення;
    3 - список мостів\n>>> '''))
                if task_type == 1:
                    print('Список компонент звʼязності графа:')
                    print(connected_component(read_graph(path_to_file, 1, 3)))
                elif task_type == 2:
                    print('Точки сполучення:')
                    graph = read_graph(path_to_file, 1, 5)
                    graph.insert(0, [])
                    print(articulation_points(graph, 0))
                elif task_type == 3:
                    print('Мости:')
                    n = read_first_line(path_to_file)
                    print(bridges.find_bridges(
                        read_graph(path_to_file, 1, 6), n))
                else:
                    print('Такого пункту не існує')
                    continue
            else:
                print('Такого пункту не існує')
                continue
            break
        except ValueError:
            print('\n###########    Введіть номер пункту!    ###########')


main()
# import doctest
# doctest.testmod()
