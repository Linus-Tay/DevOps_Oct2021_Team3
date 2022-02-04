# Imports
# import numpy as np
from buildings import *
from buildingPools import *
from loadSavedGame import loadSavedBuildingPools, loadSavedBuildings, loadSavedGame, loadSavedTurns
from saveGame import saveGame
from copy import error
from gameMenu import gameMenu
from city import loadCity
from buildings import initBuildingPools, rollBuilding

#Variables
loc_col = []
loc_row = []

def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    choice = input(str('\nEnter your choice? '))
    # Start New Game
    if (choice == '1'):    
        print("Option 1 - Start New Game")
        playCity = loadCity('start.csv')
        buildingPools = initBuildingPools()
         # Get Random Building Options
        b1 = rollBuilding(buildingPools)
        b2 = rollBuilding(buildingPools)
        gameMenu(buildingPools,playCity,1,b1,b2)
    # Load Saved game
    elif (choice == '2'): 
        print("Option 2 - Load Save Game")
        playCity = loadSavedGame('savedGame')
        if (playCity != ''):
            buildingPools = loadSavedBuildingPools('savedBuildingPools')
            # Load Building Options
            bList = loadSavedBuildings("savedBuildings")
            status = gameMenu(buildingPools,playCity,loadSavedTurns('savedTurns'),bList[0],bList[-1])
        if status == "End":
            return False
    # Exit Menu
    elif (choice == '0'):
        return False
    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')

# Menu Menu
# while True:
#     if mainMenu() == False:
#         print('\nThank you for playing Simp City!\n')
#         break