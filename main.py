# Imports

from buildingPools import initBuildingPools, rollBuilding
from loadSavedGame import loadSavedBuildingPools, loadSavedBuildings, loadSavedGame, loadSavedTurns
from saveGame import saveGame
from copy import error
import city
from gameMenu import gameMenu


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
        # print("Option 1 - Start New Game")
        # print("Please select city map size in the dimension of row * column\n")
        # x_axis = int(input("Please enter the number of rows desired: "))
        # y_axis = int(input("Please enter the number of columns desired: "))

        # if city.validCitySize(x_axis,y_axis) == True:
        #     new_map = city.newGrid(x_axis,y_axis)
            
        #     buildingPools = initBuildingPools()   
        #     b1 = rollBuilding(buildingPools)
        #     b2 = rollBuilding(buildingPools)
        #     gameMenu(buildingPools,new_map,1,b1,b2)
        
        # else:
        #     print("Size is too big! Please keep within 40 squares!")

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