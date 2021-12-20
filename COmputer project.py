import csv
# path_to_file = input("Введіть шлях до файлу:")
# print("Чи орієнтований граф(0), чи ні(1)?")
# type = input("(0/1): ")


def read_graph(path_to_file, type, project):
    """
    :param path_to_file:
    :param type: if type == 0, graph is oriented, if type == 1, graph is not oriented 
    :return: set of tuples
    """
    from collections import defaultdict
    scc_dict = defaultdict(set)
    component = set()
    articulation_points = []
    final_set = set()
    three_2 = {}
    with open(path_to_file, 'r') as file:
        k=1
        for line in file:
            print(line)
            if k==1:
                k+=1
                length=int(line.split()[0])
                continue
            line = line.strip()
            line = line.split(" ")
            first = line[0]
            sec = line[1]
            if first in scc_dict.keys():
                scc_dict[first].add(sec)
                three_2[first].append(sec)
            else:
                scc_dict[first] = set(sec)
                three_2[first] = [sec]
            if int(type) == 1:
                if sec in scc_dict.keys():
                    scc_dict[sec].add(first)
                    three_2[sec].append(first)
                else:
                    scc_dict[sec] = set(first)
                    three_2[sec] = [first]
            final_set.add((int(first), int(sec)))
            if project == 3:
                component.add(int(first))
                component.add(int(sec))
            articulation_points = [three_2[value] for value in sorted(three_2)]
    if project == 3:
        return three_2
        component = sorted(list(component))
        return (final_set, component)
    elif project == 4:
        return (length, scc_dict)
    elif project == 5:
        return articulation_points


def write_file(file_path):
    pass


def component(graph):
    pass


def strongly_connected_component(graph):
    pass


def dfs(graph, start, d=[], h=[], ch=0, visited=None, p=-1, root=0, articulation_poins=set()):
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
        dfs(graph, next, d, h, ch, visited, start, root, articulation_poins)
        d[start] = min(d[start], d[next])
        if h[start] <= d[next] and p != -1:
            articulation_poins.add(start)
    if p == -1 and len(graph[start]) > 1:
        articulation_poins.add(0)
    articulation_poins=list(articulation_poins)
    return articulation_poins


def main():
    import scc
    path_to_file = input('    Введіть шлях до файлу:\n>>> ')
    while True:
        try: 
            type_of_graph = int(input('   Виберіть тип графу:\n    0 - якщо граф орієнтований\n    1 - якщо граф неорієнтований\n>>> '))
            task_type = int(input('''
    Виберіть що ви бажаєте дізнатись про граф (введіть номер пункту):
    1 - список компонент зв'язності (граф неорієнтований);
    2 - список компонент сильної зв'язності (граф орієнтований);
    3 - список точок сполучення;
    4 - список мостів 
    5 - Повернути всі можливі значення\n>>> ''')); break
        except ValueError: 
            print('\n########### Введіть номер пункту! ###########')

    graph = read_graph(path_to_file, type_of_graph, task_type)
    print(graph)
    print('#################################################################################################################################################################33')
    print(scc.kosaraju_scc(graph[1], graph[0]))

main()
