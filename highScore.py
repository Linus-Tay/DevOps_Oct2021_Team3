alist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH',
         'AI', 'AJ', 'AK', 'AL', 'AM', 'AN']

# print(alist[7-1]) #Get last alpha

def getHSList(dimension):
    filename = dimension[0] + "x" + dimension[-1]
    try:
        highScoreList=[]
        file=open('./highScores/{}.csv'.format(filename),'r')
        for line in file:
            lineList=[]
            templist=[]
            line = line.strip('\n')
            templist = line.split(',')
            lineList.append(templist[0])
            lineList.append(int(templist[-1]))
            highScoreList.append(lineList)
        return highScoreList
    except Exception as e:
        # No files with that Dimension
        return []

def displayHighScore(dimension):
    highScores = getHSList(dimension)
    if highScores == []:
        filename = str(dimension[0]) + "x" + str(dimension[-1])
        print("\nCurrently, there is not high score set for city size {}.\n".format(filename))
    else:
        # Print High Score
        printHeaders()
        for i in range(len(highScores)):
            print("{:>2}. {:<22}{:>5}".format(i+1,highScores[i][0],highScores[i][-1]))
        print("\n")

def printHeaders():
    print('\n{:-^31}'.format(' HIGH SCORES '))
    print("{0:>3}{1:>7}{2:>21}".format("Pos","Player","Score"))
    print("{}{:>7}{:>21}".format("---","------","-----"))
# displayHighScore(dimension,"TEST","76")

# take second element for sort
def takeSecond(elem):
    try:
        return elem[1]
    except Exception as e:
        return ''


# When game ends
def checkHighScore(dimension,playerScore):
    if (len(dimension) == 2 and isinstance(dimension, list) and 
        isinstance(dimension[0], str) and isinstance(dimension[-1], str) and 
        isinstance(playerScore, int)):
        highScores = getHSList(dimension)
        if len(highScores) == 10:
            # Player Score is higher than lowest score in High Score
            # Get lowest score in High Score list using [-1][-1] because highscore is already sorted from highest to lowest
            if playerScore > highScores[-1][-1]:
                addHighScore(dimension,playerScore,highScores)
            # Player Score is same as the lowest score in High Score
            elif playerScore == highScores[-1][-1]:
                print("\nUnfortunately, you didn't make it to the High Score List. The minimum score required is {}.".format(playerScore+1))
                return False
            # Player Score is lower than lowest score in High Score
            else:
                print("\nUnfortunately, you didn't make it to the High Score List. The minimum score required is {}.".format(highScores[-1][-1]+1))
                return False
        elif len(highScores) < 10:
            # No matter how much player score, it will be in High Score List
            addHighScore(dimension,playerScore,highScores)
    else:
        print("An error occured, parameters for checkHighScore function is invalid.")

def addHighScore(dimension,playerScore,highScores):
    playerName = input(str("Please enter your name (max 20 chars): "))
    results = []
    results.append(playerName)
    results.append(playerScore)
    highScores.append(results)
    highScores.sort(key=takeSecond,reverse=True)
    # Slice list to top 10
    highScores = highScores[ 0 : 10 ]
    filename = dimension[0] + "x" + dimension[-1]
    file=open('./highScores/{}.csv'.format(filename),'w')
    for result in highScores:
        file.write(result[0] + "," + str(result[-1]) + "\n")
    file.truncate()
    file.close()

# Dimension = ["3","4"] [x axis,y axis]
# checkHighScore(["2","4"],"test",100)
# displayHighScore(["2","4"])