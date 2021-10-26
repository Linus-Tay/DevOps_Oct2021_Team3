def mainMenu():
    print('\nWelcome, mayor of Simp City!')
    print('----------------------------')
    option_list=('Start new game','Load saved game')
    for i in range(len(option_list)):
        print('[{}] {}'.format(i+1,option_list[i]))
    print('\n[0] Exit')
    
    
while True:
    mainMenu()
    choice = input(str('\nEnter your choice? '))
    if choice=='1':
        print('New Game')
        break
    else:
        print('\nInvalid option, please try again!')
    