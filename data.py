import csv

def vector(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for line in reader:
            data.append(line)
    return data

def get_result(list):
    c = []
    for i in list:
            if i[0] > i[1]:
                c.append('1')
            if i[0] == i[1]:
                c.append('0')
            if i[0] < i[1]:
                c.append('-1')
    return c



