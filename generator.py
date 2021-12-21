"""
.csv graph file generator
"""

def print_to_file(path_to_file, final):
    """
    Prints data to .csv file
    eg. "graphs/generated_graph.csv"
    """
    filea = open(path_to_file, "w")
    filea.write(str(200)+' '+str(203)+'\n')
    for line in final:
        filea.write(str(line[0])+' '+str(line[1])+'\n')
    filea.close()

def create_data(num, path_to_file, flag = False):
    """
    Creates random data
    """
    import random
    a = []
    b = []
    final = []
    while len(a) <= num//2:
        m = random.randrange(1, num//2)
        n = random.randrange(1, num//2)
        if m!=n:
            a.append((m,n))
    while len(b) <= num//2:
        m = random.randrange(num//2+1, num)
        n = random.randrange(num//2+1, num)
        if m!=n:
            b.append((m,n))
    final = a+b
    k = (a[random.randrange(0,num//2)][0], b[random.randrange(0,num//2)][1])
    final.append(k)
    print_to_file(path_to_file, final)
    if flag:
        for elem in final:
            print(f"{elem[0]} {elem[1]}")

if __name__ == '__main__':
    try:
        num = int(input('Введіть число: '))
    except ValueError:
        print('Наступного разу введіть, будь ласка, число')
        quit()
    path_to_file = input('Введіть шлях до файлу: ')
    flag = input('Виводити текст? (1 - Так, будь-яке інше - ні): ')
    if flag == '1':
        create_data(num, path_to_file, True)
    else:
        create_data(num, path_to_file)