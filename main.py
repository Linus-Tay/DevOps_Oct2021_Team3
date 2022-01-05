# Imports
from copy import error
from gameMenu import gameMenu
from city import loadCity
from buildings import initBuildingPools, rollBuilding
#Variables

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
        print("Option 1 - Start New Save Game")
        playCity = loadCity('start.csv')
        buildingPools = initBuildingPools()
        # Get Random Building Options
        b1 = rollBuilding(buildingPools)
        b2 = rollBuilding(buildingPools)
        gameMenu(buildingPools,playCity,1,b1,b2)
            
    # Load Saved game
    elif (choice == '2'): 
        print("Option 2 - Load Save Game")
    # Exit Menu
    elif (choice == '0'):
        print('\nThank you for playing Simp City!\n')
        return False
    # Validate for Invalid Input
    else:
        print('\nInvalid option, please try again!')

# Menu Menu
# while True:
#     if mainMenu() == False:
#         break