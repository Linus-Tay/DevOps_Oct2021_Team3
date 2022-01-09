import numpy as np

# MenuMenu Option 2 - Load Saved Game
def loadSavedGame(filename):
    try:
        file=open('{}.csv'.format(filename),'r')
        mainCity=[]
        lineList=[]
        for line in file:
            line=line.strip('\n')
            lineList=list(line)
            mainCity.append(lineList)
        return mainCity
    except Exception as e:
        print('\nThere is no saved game.')
        return ''

# MenuMenu Option 2 - Load Saved Building Pools
def loadSavedBuildingPools(filename):
    try:
        file=open('{}.csv'.format(filename),'r')
        varList=[]
        for line in file:
            line=line.strip('\n')
            bName = str(line[0:3])
            bAmount = int(line[-1])
            var = (bName, bAmount)
            varList.append(var)
        bPools = np.array(varList, dtype=[('Building','U5'),('Copies','<i4')])
        return bPools
    except Exception as e:
        print('\nThere is no saved Building Pools.')
        return ''

# MenuMenu Option 2 - Load Saved Turns
def loadSavedTurns(filename):
    try:
        file=open('{}.csv'.format(filename),'r')
        for line in file:
            turn = int(line)
        return turn
    except Exception as e:
        print('\nThere is no saved turns.')
        return ''

def loadSavedBuildings(filename):
    try:
        file=open('{}.csv'.format(filename),'r')
        varList=[]
        for line in file:
            b1 = str(line[0:3])
            b2 = str(line[-3:])
            varList.append(b1)
            varList.append(b2)
        return varList
    except Exception as e:
        print('\nThere is no saved buildings.')
        return ''