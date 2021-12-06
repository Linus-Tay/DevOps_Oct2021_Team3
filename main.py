# Imports
from copy import error
from Buildings import *
from buildingPools import *

#Variables


#Functions

def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    

# Game Menu
def gameMenu(bPool,playCity,turn):
        if turn == 1:
                # Get Random Building Options
                b1 = rollBuilding(bPool)
                b2 = rollBuilding(bPool)

        while True:

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
                currentT = turn
                x = np.where(bPool['Building'] == b1)
                currBuild = bPool['Building'][x]
                build_loc = input(str('Build Where? '))
                
                try:
                    turn = insertBuild(playCity,bPool,build_loc,currBuild,turn)
                except Exception as e:
                    print(e)

        

  
                if turn> currentT:
                    b1 = rollBuilding(bPool)
                    b2 = rollBuilding(bPool)
             
            
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
    