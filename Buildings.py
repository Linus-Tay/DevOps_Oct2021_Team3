import csv
import copy
from buildingPools import *


row = []
col = []


'''
1. user input x and y ("C2")
2. check user input if is valid
3. get the index of x and y based on play map
4. insert x and y into row and col list 
5. validate row and col input for new building placement
6. check if new input is trying to build on existing building
7. removes from the row and col list if #7 is true
8. insert building given x and y into city map
9. checks building and given x and y validity to insert
'''
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


'''
function takes in 2 param
param 1: playMap (the array list containing the city map)
param 2: userinput (what user entered __)
return: rol and col list 
(if all pass, to be inserted row and col index will be inserted into
a rol and col list)
'''
def verifyPosition(playMap,userinput):
    # x = column, y = row
    # getting user input x and y
    # validating user input
    # locate col and row index 
    # insert into row and col 
    # return row and col
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

    # if validation pass then insert user input into row and col list
    if userInput_valid == True:
        if str.upper(x) in playMap[0]:
            col.insert(0,playMap[0].index(str.upper(x)))
    
        for i in playMap:
            for k in i:
                if k == y:
                    row.insert(0,playMap.index(i))
        return row,col

'''
function takes in 2 param
param 1: playMap (the array list containing the city map)
param 2: x (row to be inserted)
param 3: y (col to be inserted)
return: bool 
(true being theres a build adjacent to the coordinates to be buit
false being not able to build)
'''
def checkAdjBuild(arrMap,x,y):
    #print("Checking adj x:{} y:{}".format(x,y))
    #using getbuildname function to return if there is any buildings
    topBuild = getBuildName(arrMap,x-2,y)
    btmBuild = getBuildName(arrMap,x+2,y)
    leftBuild = getBuildName(arrMap,x,y-6)
    rightBuild = getBuildName(arrMap,x,y+6)

        
    #print("Left: {} Right: {} Up: {} Down: {}".format(leftBuild,rightBuild,topBuild,btmBuild))
    # only if any of the buildings returns something then return true
    if topBuild != None or btmBuild != None or leftBuild != None or rightBuild != None:
        return True
    return False


# takes in row and col to check 
# check if valid and return bool accordingly
'''
function takes in 2 param
param 1: playMap (the array list containing the city map)
param 2: userinput (coordinates to build new building)
return: bool (true being able to build and false being not able to build)
'''
def validateXYInput(playMap,user_inputs):
    print(user_inputs)
    #for testing purposes:
    # row = user_inputs[0]
    # col = user_inputs[1]
    #print("Checking row: {} and col: {} validity".format(x,y))
    #print("row: {} col: {}".format(row,col))

    new_row = user_inputs[0][0]
    new_col = user_inputs[1][0]
    old_row = user_inputs[0][1]
    old_col = user_inputs[1][1]
    
    #if user tries to build on the same location
    if old_row == new_row and old_col == new_col:
        print("Check #1 - Building on same location")
        return False
    #if user tries to build on the same column
    elif old_col == new_col:
        #print("Check #2 - Building on same Col")
        # validate the row input
        if new_row -2 == old_row or new_row + 2 == old_row:
            #check if its building on existing building
            if checkExistingBuilding(playMap,new_row,new_col) == False:
                return True
        
        #else check for any adjacent buildings
        elif checkAdjBuild(playMap,new_row,new_col) == True:
            #print("Check #2 - Adjacent building")
            return True
        else:
            return False
    #if user tries to build on the same row
    elif old_row == new_row:
        #print("Check #3 - Building on same Row")
        #validate the column input
        if new_col - 6 == old_col or new_col + 6 == old_col:
            #print("Check #3 - checking col validity")
            #check for any existing buildings
            if checkExistingBuilding(playMap,new_row,new_col) == False:
                return True
           
        elif checkAdjBuild(playMap,new_row,new_col) == True:
            print("Check #3 - Adjacent building")
            return True
        else:

            return False
    #if user tries to build a different row and different column
    #check if its adjacent building
    elif new_row - 2 == old_row or new_row + 2 == old_row or new_col - 6 == old_col or old_col + 6 == old_col:
        print("Check #4 - checking for adjacent building")
        if checkAdjBuild(playMap,new_row,new_col) == True:
            print("Check #4 adjacent building true")
            return True
        else:

            return False
    elif checkAdjBuild(playMap,new_row,new_col) == True:
        return True
    else:
        print("Check #5 Building diagonally False")
        return False
       

'''
function takes in 5 param
param 1: playMap (the array list containing the city map)
param 2: bPool (referring to the building pools)
param 3: userinput (coordinates to build new building)
param 4: bName (building name to be built)
param 5: t (user's turn)
return: t (+1 if success if not remain the same)
'''
def insertBuild(playMap, bPool, userinput, bName, t):
    x_y = verifyPosition(playMap,userinput)
   
    new_row = x_y[0][0]
    new_col = x_y[1][0]

    if t == 1:
        playMap[new_row][new_col-1] = bName[0][0]
        playMap[new_row][new_col] = bName[0][1]
        playMap[new_row][new_col+1] = bName[0][2]
        #For testing use the codes below
        # playMap[new_row][new_col-1] = bName[0]
        # playMap[new_row][new_col] = bName[1]
        # playMap[new_row][new_col+1] = bName[2]
        t+=1
        bPool = deductBPoolCopies(bPool,bName)
    elif t >1:
        # if validates is true then insert the building
        # else removes the x and y from the row and col
        if validateXYInput(playMap,x_y) == True:
            playMap[new_row][new_col-1] = bName[0][0]
            playMap[new_row][new_col] = bName[0][1]
            playMap[new_row][new_col+1] = bName[0][2]
            #For testing use the codes below            
            # playMap[new_row][new_col-1] = bName[0]
            # playMap[new_row][new_col] = bName[1]
            # playMap[new_row][new_col+1] = bName[2]
            t+=1
            bPool = deductBPoolCopies(bPool,bName)
        
        elif validateXYInput(playMap,x_y) == False:
            row.pop(0)
            col.pop(0)

    return t
        
