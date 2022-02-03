import csv
import copy

from numpy import empty

from buildingPools import initBuildingPools, rollBuilding
from gameMenu import gameMenu


def loadCity(file):
    mainCity = []
    try:
        with open(file,encoding='utf-8-sig',newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for x in spamreader:
                col = []
                for i in x:
                    if i == '*':
                        i = ' '
                    col.append(i)
                mainCity.append(col)  
        playCity=copy.deepcopy(mainCity)
        return playCity
    except:
            return False


def viewCity(map,bpool):
    city=[]
    for i in map:
        string = ''
        for char in i:
            string += char
        city.append(string)

    i = 0 
    k = 0
    # in the case where the length of city is more than building pools list
    if len(city) > len(bpool):
        while i < len(city):
            if i < len(city):
                if i == 0:
                    print("{}\t\tBuildings\tRemaining".format(city[i]))
                elif i <= len(bpool):
                    print("{}\t\t{}\t\t{}".format(city[i],bpool[k]['Building'],bpool[k]['Copies']))
                    k+=1
                else:
                    #print remaining of city
                    print("{}".format(city[i]))
            i +=1
    #case when length of building pools is longer            
    else:
        while i <= len(bpool):
            if i < len(bpool):
                if i == 0:
                    print("{}\t\tBuildings\tRemaining".format(city[i]))

                elif i < len(city):
                    # need this statment so all elements in city can be printed
                    print("{}\t\t{}\t\t{}".format(city[i],bpool[k]['Building'],bpool[k]['Copies']))
                    k +=1
                else:
                    #print remaining of building pools
                    print("{}\t\t{}\t\t{}".format(" "*len(city[0]),bpool[k]['Building'],bpool[k]['Copies']))
                    k +=1            
            else:
                #print the last item 
                print("{}\t\t{}\t\t{}".format(" "*len(city[0]),bpool[k]['Building'],bpool[k]['Copies']))
            i +=1


def validCitySize(x_axis,y_axis):
    
    if isinstance(x_axis, int)  and isinstance(y_axis, int) :
        if y_axis <= 26:
            if x_axis*y_axis > 0 and x_axis*y_axis <=40:
                return True
            else:
                print("Invalid size! Please retry with a size of minimum of 1 squares and maximum of 40 squares")
                return False
           
        else:
            print("Column size can only be up to 26, please retry!")
            return False
    else:
        print("Invalid Input! Please enter a number input!")
        return False

def newGrid(x_axis,y_axis):
    
    #final list
    main = []

    # using ASCII table to populate alphabet header list
    alphaHeader = []
    A = 65 # Dec value for 'A'
    
    # create a counter to represent row number
    row_counter = 1

    # iterate through the number of rows
    for r in range(0,x_axis):
        rowLine = []
        gridLine = []

        # girdline to start with 2 spaces
        gridLine.append("  ")

        # convert to str type here, add spaces first
        if r+1 >= 10:
            rowLine.append(""+str(row_counter))       
        else:
            rowLine.append(" "+str(row_counter))
        row_counter+=1

        # iterate through the number of columns
        for c in range(0,y_axis):

            # first row will be the alphabet header
            # 5 spaces in a square + 6th space to account for gridline
            if r == 0:
                alphaHeader.append(" ") 
                alphaHeader.append(" ")
                alphaHeader.append(chr(A))
                alphaHeader.append(" ")
                alphaHeader.append(" ")
                alphaHeader.append(" ")
                A +=1
            
            # setup the gridline row
            # each grid starts in the order of +-----
            gridLine.append("+")
            gridLine.append("-")
            gridLine.append("-")
            gridLine.append("-")
            gridLine.append("-")
            gridLine.append("-")

            # setup the numbers row
            # each row starts in the order of | + 5 spaces to form a square
            rowLine.append("|")
            rowLine.append(" ")
            rowLine.append(" ")
            rowLine.append(" ")
            rowLine.append(" ")
            rowLine.append(" ")

        # append + to gridline to end the row accordingly
        # append | to rowLine to end the row accordingly
        gridLine.append("+")
        rowLine.append("|")

        # append each row to main list in the order of gridline, rowLine
        main.append(gridLine)
        main.append(rowLine)


    # add spaces infront of alphaheader 
    alphaHeader.insert(0," ")
    alphaHeader.insert(0," ")
    alphaHeader.insert(0," ")

    # insert the alphabet header into the first item of main list
    main.insert(0,alphaHeader)

    # insert gridline to the end of main list to close the grids
    main.insert((len(main)),gridLine)
    
    playCity=copy.deepcopy(main)

    return playCity


def chooseCitySize(city_map,bPool):
    print("Choose City size with dimension of row and column")
    opt = 0
    updated = False
    while opt == 0 and updated != True:
        try:
            row = int(input("Please enter the number of rows desired: "))
            col = int(input("Please enter the number of columns desired: "))
        except ValueError:
            print("Invalid Input! Please enter a number input!")
        else:
            if validCitySize(row,col) == True:
                print("Your city map is now {}x{}: ".format(row,col))
                updated = True
                city_map = newGrid(row,col)
                viewCity(city_map,bPool)
                a_file = open("playmap.csv", "w")
                a_file.truncate()
                for i in range(len(city_map)):
                    a_file.write(str(''.join(city_map[i])))
                    a_file.write('\n')
                a_file.close()
                print("[1] re-configure city map")
                print("[0] return to previous menu")
                option = int(input("Enter your choice?"))
                if option == 1:
                    updated = False
                
                else:
                    return                  


def startNewGame(citymap,pool):
    
    print("Option 1 - Start New Game")
    b1 = rollBuilding(pool)
    b2 = rollBuilding(pool)
    gameMenu(pool,citymap,1,b1,b2)
    