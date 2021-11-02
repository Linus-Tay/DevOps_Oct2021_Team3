import numpy as np
from random import randrange
from numpy.core.numeric import roll




#Variables
main_city = []






#Functions

def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    
#initiate building pools with 8 copies of each building for new game
def initBuildingPools():
    #Beach: 3 points if it is built on the left or right side of the city, 1 point otherwise.
    #Factory: 1 point per factory in the city, up to a maximum of 4points for the first 4 factories. All subsequent factories only score 1 point each.
    #House: if its beside a factory then it scores 1 point only. Other wise it scores 1 point for each adjacent house or shop, and 2 points for each adjacent beach
    #Shop: scores 1 point per different type of building adjacent to it
    #Highway: Scores 1 point per connected highway in the same row

    #Structured array for buildings pool
    x = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
                dtype=[('Building','U5'),('Copies','<i4')])
    return x

def viewCity(map):
    for i in map:
        print(i)

#for loading of new game by reading start.txt which will load the city map
def loadCity(file):
    
    with open(file) as f:
        for i in f:
            row = []
            row.append(i.rstrip())
            for i in row:
                main_city.append(i)
    #display city 
    viewCity(main_city)
    


#randomnize 2 building for every turn
def rollBuilding(bPool):

    b = bPool[randrange(5)]['Building']
    return b
                
def viewRemainingBuilds(bPool):
    print('Buildings\tRemaining\n----------\t----------')
    for i in range(len(bPool)):
        print('{}\t\t{}'.format(bPool['Building'][i],bPool['Copies'][i]))

#load options for each turn 
def gameMenu(bPool):
        #two random building options
        b1 = rollBuilding(bPool)
        b2 = rollBuilding(bPool)

        #game options
        game_menu = [[1,'Build a ' + b1],[2,'Build a '+b2],
        [3,'See remaining buildings'],[4,'See Current Score'],
        [5,'Save Game'],[0,'Exit to main menu']]

        #displaying game options
        for i in range(len(game_menu)):
            print('[{}] {}'.format(game_menu[i][0],game_menu[i][1]))
            if i == 3:
                print()
        game_option= input(str('Your Choice?'))

        #build a building
        if game_option == '1':
            pass
        #build a building
        elif game_option == '2':
            pass
        #view remaining building available
        elif game_option == '3':
            viewRemainingBuilds(bPool)
        #view current score
        elif game_option == '4':
            pass
        #save game
        elif game_option =='5':
            pass
        #exit to main menu
        elif game_option =='0':
            return
        else:
            print("Invalid option, please try again")

        




while True:
    mainMenu()
    choice = input(str('\nEnter your choice? '))
    if choice=='1':

        print('\n----------Turn 1----------\n')
        loadCity('start.txt')
        buildingPools = initBuildingPools()
        gameMenu(buildingPools)
    elif choice =='0':
        break
    else:
        print('\nInvalid option, please try again!')
    