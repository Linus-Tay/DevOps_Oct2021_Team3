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




def getBuildName(arrMap,x,y):
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
    # userInput_valid = False

    if len(userinput) != 2:
        print("Cec")
        raise(IndexError())
        

    x = userinput[0]
    y = userinput[1]
  
    # validation check
    col_check = ["A","B","C","D"]
    if x.isalpha() and y.isnumeric() and int(y) >= 1 and int(y) < len(playMap[0]) and len(userinput) <=2:
        if x.upper() in col_check:
            return True
        else:
            raise ValueError() 
            # print("input column is invalid")
            # return None
    
    else:
        raise ValueError()

    # if validation pass then insert user input into row and col list
def retrievePos(playMap,userinput):   
    x = userinput[0]
    y = userinput[1]

    if verifyPosition(playMap,userinput) == True:
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

    #using getbuildname function to return if there is any buildings
    topBuild = getBuildName(arrMap,x-2,y)
    btmBuild = getBuildName(arrMap,x+2,y)
    leftBuild = getBuildName(arrMap,x,y-6)
    rightBuild = getBuildName(arrMap,x,y+6)

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
    new_row = user_inputs[0][0]
    new_col = user_inputs[1][0]
    old_row = user_inputs[0][1]
    old_col = user_inputs[1][1]
    
    if checkExistingBuilding(playMap,new_row,new_col) == False:
        if checkAdjBuild(playMap,new_row,new_col) == True:
            return True
        else:
            return False

    elif checkExistingBuilding(playMap,new_row,new_col) == True:
        print("Position Taken! Please try again.")
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

    x_y = retrievePos(playMap,userinput)
   
    new_row = x_y[0][0]
    new_col = x_y[1][0]

    if t == 1:
        playMap[new_row][new_col-1] = bName[0]
        playMap[new_row][new_col] = bName[1]
        playMap[new_row][new_col+1] = bName[2]
        t+=1
        bPool = deductBPoolCopies(bPool,bName)
    elif t >1:
        # if validates is true then insert the building
        # else removes the x and y from the row and col
        if validateXYInput(playMap,x_y) == True:
            playMap[new_row][new_col-1] = bName[0]
            playMap[new_row][new_col] = bName[1]
            playMap[new_row][new_col+1] = bName[2]
            t+=1
            bPool = deductBPoolCopies(bPool,bName)
        
        elif validateXYInput(playMap,x_y) == False:
            row.pop(0)
            col.pop(0)
            print("Invalid Position! Please try again.")

    return t
        