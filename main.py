# Imports

import shutil
from buildingPools import initBuildingPools, rollBuilding
from loadSavedGame import loadSavedBuildingPools, loadSavedBuildings, loadSavedGame, loadSavedTurns
from saveGame import saveGame
from copy import error
from gameMenu import gameMenu
import city
import highScore

dimension = [4,4]

def mainMenu():
    #load game with default settings
    #citymap = loadSavedGame('playmap')
    citymap = city.newGrid(dimension[1],dimension[0]) 
    # playpool = default_pool[0]
    pool = loadSavedBuildingPools('playpool')
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start New Game','Load Saved Game','Show High Scores','Settings')

    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    choice = input(str('\nEnter your choice? '))

    # Start New Game
    if (choice == '1'):
        
        city.startNewGame(citymap,pool)

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
    # Option 3 - Show High Scores
    elif (choice == '3'):
        print("\nOption 3 - Show High Scores\n")
        dimension[0] = str(dimension[0])
        dimension[-1] = str(dimension[-1])
        # Prints current dimension highscore 
        highScore.displayHighScore(dimension)
        while True:
            print("[1] View other city high score")
            print("[0] exit")
            choice = input("\nEnter your choice: ")
            if (choice == "1"):
                x_axis = int(input("Please enter the number of rows desired: "))
                y_axis = int(input("Please enter the number of columns desired: "))
                if x_axis*y_axis <= 40 and x_axis*y_axis >0:
                    newdimension = []
                    newdimension.append(str(x_axis))
                    newdimension.append(str(y_axis))
                    highScore.displayHighScore(newdimension)
                else:
                    print("\nDimension entered is invalid!")
            elif (choice == "0"):
                dimension[0] = int(dimension[0])
                dimension[-1] = int(dimension[-1])
                break
            else:
                print('\nInvalid option, please try again!')
    elif choice == '4':
        settings_menu = ('Choose City Size','Choose Building Pool')
        opt = 1
        while opt != 0:
            print("Option 4 - Settings\n")
            for x in range(len(settings_menu)):
                print("[{}] {}".format(x+1,settings_menu[x]))

            print("\n[0] Return to main menu")
            option = input(str('\nEnter your choice? '))
            if option == '1':
                city_size = city.chooseCitySize(citymap,pool)
                dimension.clear()
                dimension.append(city_size[0])
                dimension.append(city_size[1])
            else:
                opt = 0
    # Exit Menu
    elif (choice == '0'):
        return False

    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')

# Menu Menu
while True:

    if mainMenu() == False:
        print('\nThank you for playing Simp City!\n')
        break