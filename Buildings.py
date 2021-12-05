import csv
import copy
from buildingPools import *


row = []
col = []

# 1. user input x and y ("C2")
# 2. check user input if is valid
# 3. get the index of x and y based on play map
# 4. checks if play map already has input based on given x and y
# 5. insert x and y into row and col list if available
# 6. validate row and col input 
# 7. insert building given x and y into city map
# 8. checks building and given x and y validity to insert
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



def getBuildName(arrMap,x,y):

    a = arrMap[x][y-1]
    b = arrMap[x][y]
    c = arrMap[x][y+1]
    if a + b + c == "   ":
        return None
    return a + b + c

def checkExists(arrMap,x,y):
    if getBuildName(arrMap,x,y) == None:
        return False
    return True

# getting user input x and y
# validating user input
# locate col and row index 
# insert into row and col 
# return row and col
def insertRowCol(playMap,userinput):
    # x = column, y = row
    userInput_valid = False
    x = userinput[0]
    y = userinput[1]

    # validation check
    row_check = ["A","B","C","D"]
    if x.isalpha() and y.isnumeric() and int(y) >= 1 and int(y) < len(playMap[0]):
        if x.upper() in row_check:
            userInput_valid = True
        else:
            print("input column is invalid")
    
    else:
        print("invalid input")


    if userInput_valid == True:
        if str.upper(x) in playMap[0]:
            col.insert(0,playMap[0].index(str.upper(x)))
    
        for i in playMap:
            for k in i:
                if k == y:
                    row.insert(0,playMap.index(i))
        return row,col
    else:
        return None

def checkAdjBuild(arrMap,x,y):
    
   
    if y+6 < len(arrMap[0]) or y-6 > len(arrMap[0]):
        leftBuild = getBuildName(arrMap,x,y-6)
        rightBuild = getBuildName(arrMap,x,y+6)

    topBuild = getBuildName(arrMap,x-2,y)
    btmBuild = getBuildName(arrMap,x+2,y)
    
    if topBuild != "   " or btmBuild != "   " or leftBuild != "   " or rightBuild != "   ":
        return True
    return False


# takes in row and col to check 
# check if valid and return bool accordingly
def validateXYInput(playMap,x,y):
    #print("Checking row: {} and col: {} validity".format(x,y))

    old_row = row[1]
    old_col = col[1]
    if old_row == x and old_col == y:
        #print("Check #1 - Building on same location")
        row.pop(0)
        col.pop(0)
        return False
    elif old_col == y:
        #print("Check #2 - Building on same column")
        if x -2 == old_row or x + 2 == old_row:
            if checkExists(playMap,x,y) == False:
                return True
            else:
                #print("Check #2 - Building already exists")
                row.pop(0)
                col.pop(0)
                return False
        elif checkAdjBuild(playMap,x,y) == True:
            return True
        
    elif old_row == x:
        #print("Check #3 - Building on same row")
        if y - 6 == old_col or y + 6 == old_col:
            if checkExists(playMap,x,y) == False:
                return True
            else:
                #print("Check #3 - Building already exists")
                row.pop(0)
                col.pop(0)
                return False
        elif checkAdjBuild(playMap,x,y) == True:
            return True
    elif x - 2 == old_row or x + 2 == old_row or y - 6 == old_col or y + 6 == old_col:
        #print("Check #4 - checking for adjacent building")
        if checkAdjBuild(playMap,x,y) == True:
            return True
        else:
            row.pop(0)
            col.pop(0)
            return False



def insertBuild(playMap, bPool, userinput, bName, t):
    x_y = insertRowCol(playMap,userinput)
    new_row = x_y[0][0]
    new_col = x_y[1][0]
    #print("Turn: {}, Inserting row: {} col:{}".format(t,new_row,new_col))
    if t == 1:
        print("1st insertion")
        playMap[new_row][new_col-1] = bName[0][0]
        playMap[new_row][new_col] = bName[0][1]
        playMap[new_row][new_col+1] = bName[0][2]
        t+=1
        bPool = deductBPoolCopies(bPool,bName)
    elif t>1:
        #print("Turn {} insertion".format(t))
        if validateXYInput(playMap,new_row,new_col) == True:
            playMap[new_row][new_col-1] = bName[0][0]
            playMap[new_row][new_col] = bName[0][1]
            playMap[new_row][new_col+1] = bName[0][2]
            t+=1
            bPool = deductBPoolCopies(bPool,bName)
        else:
            return t

    return t
        
