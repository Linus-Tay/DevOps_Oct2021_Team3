import buildingPools
# from buildings import *
# from calculateScore import calculateScore
import city
# from saveGame import saveGame
import saveGame
import calculateScore
import buildings


# Game Menu
def gameMenu(bPool,playCity,turn,b1,b2):
    while True:
        if turn == 17:
            # Diplay Final layout
            print('\nFinal layout of Simp City:\n')
            city.viewCity(playCity,bPool)
            calculateScore.calculateScore(playCity)
            return "End"
        else:
            # Game Menu Options
            game_menu = [[1,'Build a ' + b1],[2,'Build a '+b2],[3,'See Current Score\n'],
            [4,'Save Game'],[0,'Exit to main menu']]
            
            # Diplay Turn
            print('\n-----------------------Turn {}-----------------------\n'.format(turn))

            # Display City
            city.viewCity(playCity,bPool)

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
                    turn = buildings.insertBuild(playCity,bPool,build_loc,b1,turn)
                except Exception as e:
                    print("Invalid Input, Try again")
        
                if turn> currentT:
                    b1 = buildingPools.rollBuilding(bPool)
                    b2 = buildingPools.rollBuilding(bPool)
                
                
            # GameOption 2 - Build A Building
            elif game_option == '2':
                currentT = turn
                build_loc = input(str('Build Where? '))
                
                try:
                    turn = buildings.insertBuild(playCity,bPool,build_loc,b1,turn)
                except:
                    print("Invalid Input, Please try again")
                
                    
        
                if turn> currentT:
                    b1 = buildingPools.rollBuilding(bPool)
                    b2 = buildingPools.rollBuilding(bPool)
            # GameOption 4 - View Current Score
            elif game_option == '3':
                print("Option 3, View Current Score!")
                print('\n-------------------Current Score--------------------\n')
                calculateScore.calculateScore(playCity)
            # GameOption 5 - Save Game
            elif game_option =='4':
                print("Option 4, save game!")
                saveGame.saveGame(playCity,bPool,turn,b1,b2)
                break
            # GameOption 0 - Exit To Main Menu
            elif game_option =='0':
                break
            else:
                print("\nInvalid option, please try again")
