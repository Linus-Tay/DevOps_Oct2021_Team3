# Imports
from copy import error
from game_menu import *
#Variables



def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')


# Menu Menu
while True:
    turn = 1
    mainMenu()
    choice = input(str('\nEnter your choice? '))
    # Start New Game
    if (choice == '1'):    
        playCity = loadCity('start.csv')
        buildingPools = initBuildingPools()
        gameMenu(buildingPools,playCity,turn)
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
    