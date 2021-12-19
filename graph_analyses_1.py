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
    four={}
    three=set()
    five=[]
    final_set=set()
    three_2={}
    with open(path_to_file, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            first = line[0]
            sec = line[1]
            if first in four.keys():
                four[first].add(sec)
                three_2[first].append(sec)
            else:
                four[first] = set(sec)
                three_2[first] = [sec]
            if int(type) == 1:
                if sec in four.keys():
                    four[sec].add(first)
                    three_2[sec].append(first)
                else:
                    four[sec] = set(first)
                    three_2[sec] = [first]
            final_set.add((int(first), int(sec)))
            if project == 3:
                three.add(int(first))
                three.add(int(sec))
            five=[three_2[value] for value in sorted(three_2)]
    if project == 3:
        # return three_2
        three = sorted(list(three))
        return (final_set, three)
    elif project == 4:
        return four
    elif project == 5:
        return five
