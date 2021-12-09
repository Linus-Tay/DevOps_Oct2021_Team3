import csv
import copy

def loadCity(file):
    mainCity = []
    with open(file,encoding='utf-8-sig',newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for x in spamreader:
            col = []
            for i in x:
                if i == '*':
                    i = ' '
                col.append(i)
            mainCity.append(col)  
    playCity=copy.deepcopy(mainCity)
    return playCity

def viewCity(map):
    for i in map:
        print(*i)
    print()