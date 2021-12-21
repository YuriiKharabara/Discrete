import csv
import numpy
import pandas
# path_to_file = input("Введіть шлях до файлу:")
# print("Чи орієнтований граф(0), чи ні(1)?")
# type = input("(0/1): ")
def read_graph(path_to_file, type, project):
    """
    :param path_to_file:
    :param type: if type == 0, graph is oriented, if type == 1, graph is not oriented 
    :return: set of tuples
    """
    three_2={}
    # data = pandas.read_csv(path_to_file, sep = ' ', names = ['first', 'sec'])
    # for row in pd.read_csv("new.csv"):
    #     dic = {row[0] : row[1] for row in pd.read_csv("new.csv").iterrows()}
    # return dic
    data = numpy.genfromtxt(path_to_file, delimiter=' ', skip_header = 1)
    data[:,0]
    # for index, number in enumerate(numpy.nditer(data)):
    #     diction[number] = [number]
    #     print(index, number)
    file=data.tolist()
    # return file
    # print(data['first'])
    for line in data:
        first = int(line[0])
        sec = int(line[1])
        if first in three_2.keys():
            three_2[first].append(sec)
        else:
            three_2[first] = [sec]
        if sec in three_2.keys():
            continue
        else:
            three_2[sec] = []
        if int(type) == 1:
            if sec in three_2.keys():
                three_2[sec].append(first)
            else:
                three_2[sec] = [first]
    if project == 3:
        return three_2
    # elif project == 4:
    #     return four
    elif project == 5:
        five=[three_2[value] for value in sorted(three_2)]
        return five
# print(read_graph(r'graph_5000_248580_1.csv', 0, 5))
# # print(read_graph(r'new.csv', 0, 4))
# print(read_graph(r'graph_5000_247404_0.csv', 1, 5))
print(read_graph(r'graph_100000_4998622_1.csv', 1, 5))
# print(read_graph(r'new.csv', 0, 3))
# print(read_graph(r'new.csv', 1, 3))