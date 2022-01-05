import csv
import copy

def loadCity(file):
    mainCity = []
    try:
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
    except:
            return False
def viewCity(map):
    # print(map)
    city=[]
    for i in map:
        string = ''
        for char in i:
            string += char
        city.append(string)
    for i in city:
        print(i)
    print('')