# Imports

from buildingPools import initBuildingPools, rollBuilding
from loadSavedGame import loadSavedBuildingPools, loadSavedBuildings, loadSavedGame, loadSavedTurns
from saveGame import saveGame
from copy import error
import city
from gameMenu import gameMenu
import city

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
        city.startNewGame()

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

    elif choice =='5':
        playCity = city.newGrid(2,5)
        buildingPools = loadSavedBuildingPools('savedBuildingPools')
        city.viewCity(playCity,buildingPools)
    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')

# Menu Menu
# while True:
#     if mainMenu() == False:
#         print('\nThank you for playing Simp City!\n')
#         break