from buildingPools import *
from buildings import *
from calculateScore import calculateScore
from city import viewCity
from saveGame import saveGame

# Game Menu
def gameMenu(bPool,playCity,turn,b1,b2):
    while True:
        if turn == 17:
            # Diplay Final layout
            print('\nFinal layout of Simp City:\n')
            viewCity(playCity)
            calculateScore(playCity)
            return "End"
        else:
            # Game Menu Options
            game_menu = [[1,'Build a ' + b1],[2,'Build a '+b2],
            [3,'See remaining buildings'],[4,'See Current Score\n'],
            [5,'Save Game'],[0,'Exit to main menu']]
            
            # Diplay Turn
            print('\n-----------------------Turn {}-----------------------\n'.format(turn))

            # Display City
            viewCity(playCity)

            # Display Game Menu Options
            for i in range(len(game_menu)):
                print('[{}] {}'.format(game_menu[i][0],game_menu[i][1]))
            
            # Prompt For User's Choice
            game_option= input(str('\nYour Choice? '))

            # GameOption 1 - Build A Building
            if game_option == '1':
                currentT = turn
                build_loc = input(str('Build Where? '))
                
                try:
                    turn = insertBuild(playCity,bPool,build_loc,b1,turn)
                except Exception as e:
                    print("Invalid Input, Try again")
        
                if turn> currentT:
                    b1 = rollBuilding(bPool)
                    b2 = rollBuilding(bPool)
                
                
            # GameOption 2 - Build A Building
            elif game_option == '2':
                currentT = turn
                build_loc = input(str('Build Where? '))
                
                try:
                    turn = insertBuild(playCity,bPool,build_loc,b1,turn)
                except:
                    print("Invalid Input, Please try again")
                    
        
                if turn> currentT:
                    b1 = rollBuilding(bPool)
                    b2 = rollBuilding(bPool)
            # GameOption 3 - View Remaining Building Available
            elif game_option == '3':
                print("Option 3, View Remaining Building Available!")
                viewRemainingBuilds(bPool)
            # GameOption 4 - View Current Score
            elif game_option == '4':
                print("Option 4, View Current Score!")
                print('\n-------------------Current Score--------------------\n')
                calculateScore(playCity)
            # GameOption 5 - Save Game
            elif game_option =='5':
                print("Option 5, save game!")
                saveGame(playCity,bPool,turn,b1,b2)
                break
            # GameOption 0 - Exit To Main Menu
            elif game_option =='0':
                break
            else:
                print("\nInvalid option, please try again")
