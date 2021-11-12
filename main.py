# Imports
import numpy as np
import csv
import copy
from random import randrange
from numpy.core.numeric import roll


#Variables
loc_col = []
loc_row = []


#Functions

def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    


def viewCity(map):
    for i in map:
        print(*i)
    print()


#for loading of new game by reading start.txt which will load the city map
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

                
def viewRemainingBuilds(bPool):
    print('Buildings\tRemaining\n----------\t----------')
    for i in range(len(bPool)):
        print('{}\t\t{}'.format(bPool['Building'][i],bPool['Copies'][i]))

#----------------------------Building functions----------------------------

#initiate building pools with 8 copies of each building for new game
def initBuildingPools():
    #Structured array for buildings pool
    buildingPools = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
                dtype=[('Building','U5'),('Copies','<i4')])
    return buildingPools

#randomnize 2 building for every turn
def rollBuilding(bPool):
    b = bPool[randrange(5)]['Building']
    return b

#Inserting coordinates(col,row) given by user into column and row list
def insertRowCol(arr,r,c):  
    if str.upper(c) in arr[0]:
        loc_col.insert(0,arr[0].index(str.upper(c)))
        #print("INSERTING COL: {} ".format(loc_col[0]))
    for i in arr:
        for x in i:
            if x == r:
                loc_row.insert(0,arr.index(i))
                #print("Inserting row: {} ".format(loc_row[0]))
    #print("Inserted rows: {}".format(loc_row))
    #print("Inserted col: {}".format(loc_col))

#sub function(insertBuilding) required to remove coords from the col & row list 
#in the case where user entered an invalid input for building           
def removeRowCol():
    loc_col.pop(0)
    loc_row.pop(0)

#sub function required(insertBuilding) to checks if there is any existing buildings
def checkExist(arr,r,c):
    if arr[r][c] == " ":
            return False
    else:
        print("You are trying to build on existing building!")
        return True

#Sub function of (insertBuilding) to perform swapping of 'item' in the city list
def mSwap(arr,bName,row,col):
    arr[row[0]][col[0]-1] = bName[0][0]
    arr[row[0]][col[0]] = bName[0][1]
    arr[row[0]][col[0]+1] = bName[0][2]

#sub function(insertBuilding) required to do the necessary validation checks when user inserts a building
#True = can build, False = cannot build
#row/col[1] refers to the previous inserted coords
#row/col[0] refers to the inserting coords
def checkCord(arr,row,col):
    print("rows: {}".format(row))
    print("cols: {}".format(col))
    #situation where trying to insert into same row & col
    if col[1] == col[0] and row[1] == row[0]:
            print("You are trying to build on existing Building!")
            #remove cordinates from col/row list
            removeRowCol()
            return False
    #situation where same column or row insertion
    elif col[1] == col[0]:
        print("check #1")
        if row[1] - 2 == row[0] or row[1] + 2 == row[0]:
            if checkExist(arr,row[0],col[0]) == False:
                return True
            else:
                print("Building at row: {} already exists or invalid".format(row[0]))
                removeRowCol()
                return False
        else:
            print("Row Input: {} is invalid".format(row[0]))
            removeRowCol()
            return False
    elif row[1] == row[0]:
        print("check #2")
        if col[1] - 6 == col[0] or col[1] + 6 == col[0]:
            if checkExist(arr,row[0],col[0]) == False:
                return True
            else:
                print("Building at col: {} already exists or invalid".format(col[0]))
                removeRowCol()
                return False  
        else:
            print("Col input: {} is invalid".format(col[0]))
            removeRowCol()
            return False
    elif row[1] - 2 == row[0] or row[1] + 2 == row[0] or col[1] - 6 == col[0] or col[1] + 6 == col[0]:
            print("check #3")
            print("You cannot build diagonally, please retry!")
            removeRowCol()
            return False

#the main function for inserting a building including all the checks and sub functions
def insertBuilding(arr,bPool,bName,row,col,t):
    insertRowCol(arr,row,col)
    r = loc_row
    c = loc_col
    if t == 1:
        mSwap(arr,bName,r,c)
        x = np.where(bPool['Building']==bName)
        index = x[0][0]
        bPool[index]['Copies']-=1
        t +=1
        #inserted_Buildings.insert(0, bName)
        #checkCityScore(arr,bName)
    elif t > 1:
        if checkCord(arr,r,c) == True:
            mSwap(arr,bName,r,c)
            x = np.where(bPool['Building']==bName)
            index = x[0][0]
            bPool[index]['Copies']-=1
            t+=1
            #inserted_Buildings.insert(0, bName)
            #checkCityScore(arr,bName)
    return (bPool)

#---------------------end of Building functions----------------------------

# Game Menu
def gameMenu(bPool,playCity,turn):

        while True:
            # Get Random Building Options
            b1 = rollBuilding(bPool)
            b2 = rollBuilding(bPool)

            # Game Menu Options
            game_menu = [[1,'Build a ' + b1],[2,'Build a '+b2],
            [3,'See remaining buildings'],[4,'See Current Score'],
            [5,'Save Game'],[0,'Exit to main menu']]
            
            # Diplay Turn
            print('\n-----------------------Turn {}-----------------------\n'.format(turn))

            # Display City
            viewCity(playCity)

            # Display Game Menu Options
            for i in range(len(game_menu)):
                print('[{}] {}'.format(game_menu[i][0],game_menu[i][1]))
                if i == 3:
                    print()
            
            # Prompt For User's Choice
            game_option= input(str('\nYour Choice? '))

            # GameOption 1 - Build A Building
            if game_option == '1':
                #get index of building from bPool to retrieve building name
                x = np.where(bPool['Building'] == b1)
                currBuild = bPool['Building'][x]

                build_loc = input(str('Build Where? '))
                print("col to search {} row to search {}".format(build_loc[0], build_loc[1]))
                bPool = insertBuilding(playCity,bPool,currBuild,build_loc[1],build_loc[0],turn)
                turn +=1
            # GameOption 2 - Build A Building
            elif game_option == '2':
               #get index of building from bPool to retrieve building name
                x = np.where(bPool['Building'] == b1)
                currBuild = bPool['Building'][x]

                build_loc = input(str('Build Where? '))
                print("col to search {} row to search {}".format(build_loc[0], build_loc[1]))
                bPool = insertBuilding(playCity,bPool,currBuild,build_loc[1],build_loc[0],turn)
                turn +=1
            # GameOption 3 - View Remaining Building Available
            elif game_option == '3':
                viewRemainingBuilds(bPool)
            # GameOption 4 - View Current Score
            elif game_option == '4':
                pass
            # GameOption 5 - Save Game
            elif game_option =='5':
                pass
            # GameOption 0 - Exit To Main Menu
            elif game_option =='0':
                return
            else:
                print("\nInvalid option, please try again")

        



# Menu Menu
while True:
    mainMenu()
    choice = input(str('\nEnter your choice? '))
    # Start New Game
    if (choice == '1'):    
        playCity = loadCity('start.csv')
        buildingPools = initBuildingPools()
        gameMenu(buildingPools,playCity,turn=1)
    # Load Saved game
    elif (choice == '2'): 
        pass
    # Exit Menu
    elif (choice == '0'):
        print('\nThank you for playing Simp City!\n')
        break
    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')
    