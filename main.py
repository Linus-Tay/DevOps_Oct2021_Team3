# Imports

import shutil
from buildingPools import chooseBuildingPools, initBuildingPools, rollBuilding
from loadSavedGame import loadSavedBuildingPools, loadSavedBuildings, loadSavedGame, loadSavedTurns
from saveGame import saveGame
from copy import error
import city
from gameMenu import gameMenu
import shutil

dimension = [4,4]
initpool = initBuildingPools('BCH','FAC','HSE','SHP','HWY')
default_pool =[initpool]
def mainMenu():
    #load game with default settings
    #citymap = loadSavedGame('playmap')
    citymap = city.newGrid(dimension[1],dimension[0]) 
    playpool = default_pool[0]
    #pool = loadSavedBuildingPools('playpool')
    
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game','View High Score','Settings')

    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    choice = input(str('\nEnter your choice? '))

    # Start New Game
    if (choice == '1'):
        
        city.startNewGame(citymap,playpool)

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
                city_size = city.chooseCitySize(citymap,playpool)
                dimension.insert(0,city_size[0])
                dimension.insert(0,city_size[1])
            elif option == '2':
                chosen_Pool = chooseBuildingPools()
                playpool = initBuildingPools(chosen_Pool[0],chosen_Pool[1],chosen_Pool[2],chosen_Pool[3],chosen_Pool[4])
                default_pool.insert(0,playpool)
            else:
                opt = 0
    
    # Exit Menu
    elif choice == '0':
       return False

    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')

# Menu Menu
while True:
    if mainMenu() == False:
        print('\nThank you for playing Simp City!\n')
        break