import csv
# path_to_file = input("Введіть шлях до файлу:")
# print("Чи орієнтований граф(0), чи ні(1)?")
# type = input("(0/1): ")


def read_graph(path_to_file, type, project):
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
    import css
    path_to_file = input('    Введіть шлях до файлу:\n>>> ')
    while True:
        try: 
            type_of_graph = int(input('   Виберіть тип графу:\n    0 - якщо граф орієнтований\n    1 - якщо граф неорієнтований\n>>> '))
            if type_of_graph == 0:
                print("Список компонент сильної зв'язності")
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
    print(css.tarjan_scc(graph[1], graph[0]))

main()
