from numpy import number
from buildingPools import *

#====================================================================================================#

'''
1. user gives an input 
    - checks if input is valid (letter-number)
    - display error message accordingly to wrong input given
2. if input is valid, retrieve the index of letter-number based on play map
3. if its first turn, user can insert anywhere
4. check validity of letter-number given on 2nd turn onwards
    - check exisiting building
    - check adjacent building
5. insert building if valid
'''



#====================================================================================================#

'''
retrieve building name from the play map given x(row) ,y(Column)
param 1: playMap (the array list containing the city map)
param 2,3: x,y (index of letter-number based on playmap)
return: returns if theres a building else return none
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

#====================================================================================================#

'''
check if x,y on play map has building using getbuildname
param 1: playMap (the array list containing the city map)
param 2,3: x,y (index of letter-number based on playmap)
return: boolean accordingly
'''
def checkExistingBuilding(arrMap,x,y):
    if getBuildName(arrMap,x,y) == None:
        return False
    return True

#====================================================================================================#

'''
verify if input given by user is a valid letter-number
param 1: playMap (the array list containing the city map)
param 2: userinput (what user entered __)
return: boolean accordingly
'''
def verifyPosition(playMap,userinput):

    # have a check for letter and number
    letter_check = False
    number_check = False
    
    # if user gives a valid 2 character input
    if len(userinput) == 2:
        x = userinput[0]
        y = userinput[1]
        #check if letter given is as according to one of the available column
        if x.upper() in playMap[0]:
            letter_check = True
        else:
            print("Invalid Letter given, Please try again with a letter-number input based on the map !")
        #check if number given is within the range of the row
        if y.isnumeric() and int(y) > 0 and int(y) <=4 :
            number_check = True
        else:
            print("Invalid Number given, Please try again with a letter-number input based on the map !")
    #if user tries an empty input
    elif userinput == "":
        print("No input given! Please try again with a letter-number input!")
    #
    else:
        print("Invalid Input! Please try again with a letter-number input!")


    #if letter and number check is true, return true as valid input else false
    if letter_check == True and number_check == True:
        return True
    else:
        return False
    
#====================================================================================================#

'''
retrieve the index of letter-number given based on the playmap and return the row and col index
this is assuming letter-number given has gone through validity checks
param 1: playMap (the array list containing the city map)
param 2,3: x,y (index of letter-number based on playmap)
return: row and col index 
'''
def retrievePos(playMap,new_row,new_col):   

    x = new_row
    y = new_col
    
    row = 0
    col = playMap[0].index(str.upper(x))     
    for i in playMap:
        for k in i:
            if k == y:
                row = playMap.index(i)

    return row,col

#====================================================================================================#

'''
Checks for adjacent building to any exisiting building
param 1: playMap (the array list containing the city map)
param 2,3: x,y (index of letter-number based on playmap)
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

#====================================================================================================#

'''
Validate if position given is true
checks for exisiting building and adjacent building
param 1: playMap (the array list containing the city map)
param 2,3: x,y (index of letter-number based on playmap)
return: bool (true being able to build and false being not able to build)
'''
def validatePosition(playmap,new_row,new_col):

    if checkExistingBuilding(playmap,new_row,new_col) == False:
        if checkAdjBuild(playmap,new_row,new_col) == True:
            return True
        else:
            print("Invalid Position, Please try again!")
            return False
    else:
        print("Building already exists! Please try another location!")   

#====================================================================================================#

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

    new_row = 0
    new_col = 0

    #if given input is valid, retrieve row and column index from play map
    if verifyPosition(playMap,userinput) == True:
        x_y = retrievePos(playMap,userinput[0],userinput[1])
        new_row = x_y[0]
        new_col = x_y[1]

    # only if theres a retrieved position == valid
    if new_row != 0 and new_col != 0:
        # user can insert anywhere on turn 1
        if t == 1:
            playMap[new_row][new_col-1] = bName[0]
            playMap[new_row][new_col] = bName[1]
            playMap[new_row][new_col+1] = bName[2]
            t+=1
            bPool = deductBPoolCopies(bPool,bName)
        # validate position on turn 2 onwards
        else:
            if validatePosition(playMap,new_row,new_col) == True:
                playMap[new_row][new_col-1] = bName[0]
                playMap[new_row][new_col] = bName[1]
                playMap[new_row][new_col+1] = bName[2]
                t+=1
                bPool = deductBPoolCopies(bPool,bName)
    return t
        
