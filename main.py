# Imports

import shutil
from buildingPools import initBuildingPools, rollBuilding
from loadSavedGame import loadSavedBuildingPools, loadSavedBuildings, loadSavedGame, loadSavedTurns
from saveGame import saveGame
from copy import error
import city
from gameMenu import gameMenu
import city


def mainMenu():
    #load game with default settings
    citymap = loadSavedGame('playmap')
    pool = loadSavedBuildingPools('playpool')

    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game','Building Settings')

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
    elif choice == '3':
        settings_menu = ('Choose City Size','Choose Building Pool')
        opt = 1
        while opt != 0:
            print("Option 3 - Building Settings")
            for x in range(len(settings_menu)):
                print("[{}] {}".format(x+1,settings_menu[x]))
            print("[0] Return to previous menu")
            option = input(str('\nEnter your choice? '))
            if option == '1':
                city.chooseCitySize(citymap,pool)
            else:
                opt = 0


    
    # Exit Menu
    elif (choice == '0'):
        # Leave a goodbye message
        print("All building settings resetted to default! See you again")
        # reset Building Settings by doing a copy 
        shutil.copyfile('defaultmap.csv','playmap.csv')
        shutil.copyfile('defaultpool.csv','playpool.csv')
        return False

    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')

# Menu Menu
# while True:
#     if mainMenu() == False:
#         print('\nThank you for playing Simp City!\n')
#         break