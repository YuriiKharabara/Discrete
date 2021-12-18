path_to_file = input("Введіть шлях до файлу:")
print("Чи орієнтований граф(0), чи ні(1)?")
type = input("(0/1): ")
def read_graph(path_to_file, type):
    """
    :param path_to_file:
    :param type: if type == 0, graph is oriented, if type == 1, graph is not oriented 
    :return: set of tuples
    """
    new_set = set()
    with open(path_to_file, 'r') as file:
        for line in file:
            line = line.strip()
            one_line = tuple(line.split(" "))
            final_set.add(one_line)
            # final_set = {(2,1), (1,4), (3,2), (3,1), (3,4), (3,5), (4,5)}
            if int(type) == 1:
                one_line = list(one_line)
                if one_line[0] != one_line[1]:
                    new = tuple([one_line[1], one_line[0]])
                    new_set.add(new)
        final_set.update(new_set)
# final_set = {(1, 3), (1, 2), (3, 4), (2, 1), (4, 3), (3, 1), (5, 4), (1, 4), (2, 3), (4, 5), (5, 3), (3, 2), (4, 1), (3, 5)}
    return final_set
