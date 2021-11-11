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
def insertColRow(arr,letter,number):               
    for i in arr:
        if number in i:
            loc_row.insert(0,arr.index(i))
            break
        for x in i:
            if  x == letter:
                loc_col.insert(0,i.index(x))
                break

#sub function(insertBuilding) required to remove coords from the col & row list 
#in the case where user entered an invalid input for building           
def removeColRow():
    loc_col.pop(0)
    loc_row.pop(0)

#sub function required(insertBuilding) to checks if there is any existing buildings
def checkExist(arr,nRow,nCol):
    if arr[nRow[0]][nCol[0]] == " ":
            return False
    else:
        print("You are trying to build on existing building!")
        return True

#Sub function of (insertBuilding) to perform swapping of 'item' in the city list
def mSwap(arr,bName,row,col,t):
    if t == 1:
        arr[row[0]][col[0]-1] = bName[0][0]
        arr[row[0]][col[0]] = bName[0][1]
        arr[row[0]][col[0]+1] = bName[0][2]
    else:
        arr[row[0]][col[0]-1] = bName[0][0]
        arr[row[0]][col[0]] = bName[0][1]
        arr[row[0]][col[0]+1] = bName[0][2]

#sub function(insertBuilding) required to do the necessary validation checks when user inserts a building
#True = can build
#False = cannot build
def checkCord(arr,nRow,nCol,oRow,oCol):
    #situation where trying to insert into same row & col
    if nCol[0] == oCol and nRow[0] == oRow:
            print("You are trying to build on existing Building!")
            #remove cordinates from col/row list
            removeColRow()
            return False
    #situation where same column insertion
    elif nCol[0] == oCol or nRow[0] == oRow:
        if nRow[0] - 2 == oRow or nRow[0] + 2 == oRow or nCol[0] - 6 == oCol or nCol[0] + 6 == oCol:
            if checkExist(arr,nRow,nCol) == False:
                return True
            else:
                print("Building already exists at where you try to build")
                removeColRow()
                return False
        else:
            print("Invalid input, please try again!")
            removeColRow()
            return False
    else:
        if nRow[0] - 2 == oRow or nRow[0] + 2 == oRow or nCol[0] - 6 == oCol or nCol[0] + 6 == oCol:
            if checkExist(arr,nRow,nCol) == False:
                return True
            else:
                print("Building already exists at where you try to build")
                removeColRow()
                return False
        else:
            print("Invalid input, please try again!")
            removeColRow()
            return False 

#the main function for inserting a building including all the checks and sub functions
def insertBuilding(arr,bPool,bName,row,col,t):
    if t == 1:
        mSwap(arr,bName,row,col,t)
        x = np.where(bPool['Building']==bName)
        index = x[0][0]
        bPool[index]['Copies']-=1
        t +=1
        
    elif t > 1:
        if checkCord(arr,row,col,loc_row[1],loc_col[1]) == True:
            mSwap(arr,bName,row,col,t)
            x = np.where(bPool['Building']==bName)
            index = x[0][0]
            bPool[index]['Copies']-=1 
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
                # print("col to search {} row to search {}".format(build_loc[0], type(build_loc[1])))
                insertColRow(playCity,build_loc[0].upper(),build_loc[1])
                col = loc_col
                row = loc_row
                bPool = insertBuilding(playCity,bPool,currBuild,row,col,turn)
                turn +=1
            # GameOption 2 - Build A Building
            elif game_option == '2':
               #get index of building from bPool to retrieve building name
                x = np.where(bPool['Building'] == b1)
                currBuild = bPool['Building'][x]

                build_loc = input(str('Build Where? '))
                # print("col to search {} row to search {}".format(build_loc[0], type(build_loc[1])))
                insertColRow(playCity,build_loc[0].upper(),build_loc[1])
                col = loc_col
                row = loc_row
                bPool = insertBuilding(playCity,bPool,currBuild,row,col,turn)
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
    