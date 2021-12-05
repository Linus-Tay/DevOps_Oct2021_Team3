import numpy as np
from random import randrange
from numpy.core.numeric import roll

#Functions
def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')

#MainMenu
while True:
    mainMenu()
    choice = input(str('\nEnter your choice? '))
    if choice=='1':
        print("\noption 1")
    elif choice =='2':
        print("\noption 2")
    elif (choice == '0'):
        print('\nThank you for playing Simp City!')
        break
    else:
        print('\nInvalid option, please try again!')
    