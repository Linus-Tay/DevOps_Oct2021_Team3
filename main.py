# Imports
import numpy as np
import csv
import copy
from random import randrange
from numpy.core.numeric import roll


#Variables


#Functions

def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    
#initiate building pools with 8 copies of each building for new game
def initBuildingPools():
    #Beach: 3 points if it is built on the left or right side of the city, 1 point otherwise.
    #Factory: 1 point per factory in the city, up to a maximum of 4points for the first 4 factories. All subsequent factories only score 1 point each.
    #House: if its beside a factory then it scores 1 point only. Other wise it scores 1 point for each adjacent house or shop, and 2 points for each adjacent beach
    #Shop: scores 1 point per different type of building adjacent to it
    #Highway: Scores 1 point per connected highway in the same row

    #Structured array for buildings pool
    buildingPools = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
                dtype=[('Building','U5'),('Copies','<i4')])
    return buildingPools

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


#randomnize 2 building for every turn
def rollBuilding(bPool):

    b = bPool[randrange(5)]['Building']
    return b
                
def viewRemainingBuilds(bPool):
    print('Buildings\tRemaining\n----------\t----------')
    for i in range(len(bPool)):
        print('{}\t\t{}'.format(bPool['Building'][i],bPool['Copies'][i]))

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
                pass
            # GameOption 2 - Build A Building
            elif game_option == '2':
               pass
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
    