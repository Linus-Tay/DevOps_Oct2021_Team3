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



def getBuildName(arrMap,x,y):
    #print("len: {}".format(len(arrMap[0])))
    #print("getting build name for x: {} y: {}".format(x,y))
    
    if x == 0 or x == len(arrMap) or y > len(arrMap[0]) or y <0:
        return None
    else:
        a = arrMap[x][y-1]
        b = arrMap[x][y]
        c = arrMap[x][y+1]
        if a + b + c == "   ":
            return None
        return a + b + c

def checkExistingBuilding(arrMap,x,y):
    if getBuildName(arrMap,x,y) == None:
        return False
    return True

# getting user input x and y
# validating user input
# locate col and row index 
# insert into row and col 
# return row and col
def verifyPosition(playMap,userinput):
    # x = column, y = row
    userInput = False
    x = userinput[0]
    y = userinput[1]
  
    # validation check
    row_check = ["A","B","C","D"]
    if x.isalpha() and y.isnumeric() and int(y) >= 1 and int(y) < len(playMap[0]) and len(userinput) <=2:
        if x.upper() in row_check:
            userInput_valid = True
        else:
            print("input column is invalid")
            return None
    
    else:
        print("#1 invalid input")
        return None


    if userInput_valid == True:
        if str.upper(x) in playMap[0]:
            col.insert(0,playMap[0].index(str.upper(x)))
    
        for i in playMap:
            for k in i:
                if k == y:
                    row.insert(0,playMap.index(i))
        return row,col

 

def checkAdjBuild(arrMap,x,y):

    #print("Checking adj x:{} y:{}".format(x,y))
    topBuild = getBuildName(arrMap,x-2,y)
    btmBuild = getBuildName(arrMap,x+2,y)
    leftBuild = getBuildName(arrMap,x,y-6)
    rightBuild = getBuildName(arrMap,x,y+6)

        
    #print("Left: {} Right: {} Up: {} Down: {}".format(leftBuild,rightBuild,topBuild,btmBuild))
    if topBuild != None or btmBuild != None or leftBuild != None or rightBuild != None:
        return True
    return False


# takes in row and col to check 
# check if valid and return bool accordingly
def validateXYInput(playMap,user_inputs):
    print(user_inputs)
    #for testing purposes:
    row = user_inputs[0]
    col = user_inputs[1]
    #print("Checking row: {} and col: {} validity".format(x,y))
    #print("row: {} col: {}".format(row,col))
    new_row = user_inputs[0][0]
    new_col = user_inputs[1][0]
    old_row = user_inputs[0][1]
    old_col = user_inputs[1][1]
  
    if old_row == new_row and old_col == new_col:
        print("Check #1 - Building on same location")
        # row.pop(0)
        # col.pop(0)
        return False
    elif old_col == new_col:
        print("Check #2 - Building on same Col")
        if new_row -2 == old_row or new_row + 2 == old_row:
            if checkExistingBuilding(playMap,new_row,new_col) == False:
                return True
            
        elif checkAdjBuild(playMap,new_row,new_col) == True:
            print("Check #2 - Adjacent building")
            return True
        else:
            print("Check #2 - Building already exists")
            # row.pop(0)
            # col.pop(0)
            return False
        
    elif old_row == new_row:
        print("Check #3 - Building on same Row")
        if new_col - 6 == old_col or new_col + 6 == old_col:
            print("Check #3 - checking col validity")
            if checkExistingBuilding(playMap,new_row,new_col) == False:
                return True
           
        elif checkAdjBuild(playMap,new_row,new_col) == True:
            print("Check #3 - Adjacent building")
            return True
        else:
            # row.pop(0)
            # col.pop(0)
            return False
    elif new_row - 2 == old_row or new_row + 2 == old_row or new_col - 6 == old_col or old_col + 6 == old_col:
        print("Check #4 - checking for adjacent building")
        if checkAdjBuild(playMap,new_row,new_col) == True:
            print("Check #4 adjacent building true")
            return True
        else:
            # row.pop(0)
            # col.pop(0)
            return False
    elif checkAdjBuild(playMap,new_row,new_col) == True:
        return True
    else:

        # if checkAdjBuild(playMap,new_row,new_col) == True:
        #     print("Check #5 adjacent building true")
        #     return True
        # else:
        print("Check #5 Building diagonally False")
        # row.pop(0)
        # col.pop(0)
        return False
       



def insertBuild(playMap, bPool, userinput, bName, t):
    x_y = verifyPosition(playMap,userinput)
    
    #print(x_y)
    
    new_row = x_y[0][0]
    new_col = x_y[1][0]

    #print("Turn: {}, Inserting row: {} col:{}".format(t,new_row,new_col))
    if t == 1:
        #print("1st insertion")
        # playMap[new_row][new_col-1] = bName[0][0]
        # playMap[new_row][new_col] = bName[0][1]
        # playMap[new_row][new_col+1] = bName[0][2]
        #For testing use the codes below
        playMap[new_row][new_col-1] = bName[0]
        playMap[new_row][new_col] = bName[1]
        playMap[new_row][new_col+1] = bName[2]
        t+=1
        bPool = deductBPoolCopies(bPool,bName)
    elif t >1:
        #print("Turn {} insertion".format(t))
        #print(x_y)
        if validateXYInput(playMap,x_y) == True:
            # if checkAdjBuild(playMap,new_row,new_col) == True:
            # playMap[new_row][new_col-1] = bName[0][0]
            # playMap[new_row][new_col] = bName[0][1]
            # playMap[new_row][new_col+1] = bName[0][2]
            #For testing use the codes below            
            playMap[new_row][new_col-1] = bName[0]
            playMap[new_row][new_col] = bName[1]
            playMap[new_row][new_col+1] = bName[2]
            t+=1
            bPool = deductBPoolCopies(bPool,bName)
        elif validateXYInput(playMap,x_y) == False:
            row.pop(0)
            col.pop(0)
        # elif validateXYInput(playMap,x_y) == False:
        #     if checkAdjBuild(playMap,new_col,new_col) == True:
        #         playMap[new_row][new_col-1] = bName[0][0]
        #         playMap[new_row][new_col] = bName[0][1]
        #         playMap[new_row][new_col+1] = bName[0][2]
        #         # playMap[new_row][new_col-1] = bName[0]
        #         # playMap[new_row][new_col] = bName[1]
        #         # playMap[new_row][new_col+1] = bName[2]
        #         t+=1
        #         bPool = deductBPoolCopies(bPool,bName)
                
    

    return t
        
