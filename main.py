# Imports
from highScore import displayHighScore
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
    option_list=('Start New Game','Load Saved Game','Show High Scores')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    choice = input(str('\nEnter your choice? '))
    # Option 1 - Start New Game
    if (choice == '1'):    
        print("Option 1 - Start New Game")
        playCity = loadCity('start.csv')
        buildingPools = initBuildingPools()
         # Get Random Building Options
        b1 = rollBuilding(buildingPools)
        b2 = rollBuilding(buildingPools)
        gameMenu(buildingPools,playCity,1,b1,b2)
    # Option 2 - Load Saved game
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
    # Option 3 - Show High Scores
    elif (choice == '3'):
        print("\nOption 3 - Show High Scores\n")
        x_axis = int(input("Please enter the number of rows desired: "))
        y_axis = int(input("Please enter the number of columns desired: "))
        if x_axis*y_axis <= 40 and x_axis*y_axis >0:
            dimension = []
            dimension.append(str(x_axis))
            dimension.append(str(y_axis))
            displayHighScore(dimension)
        else:
            print("\nDimension entered is invalid!")
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