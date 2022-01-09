# Game Option 5 - Save Game
def saveGame(playCity,bPool,turn,b1,b2):
    file=open('savedGame.csv','w')
    for i in range(len(playCity)):
        file.write(str(''.join(playCity[i])))
        file.write('\n')
    file.close()
    file=open('savedBuildingPools.csv','w')
    for i in range(len(bPool)):
        file.write(str(bPool[i][0]))
        file.write(',')
        file.write(str(bPool[i][-1]))
        file.write('\n')
    file.close()
    file=open('savedTurns.csv','w')
    file.write(str(turn))
    file.close()
    file=open('savedBuildings.csv','w')
    file.write(str(b1) + "," + str(b2))
    file.close()
    print('\nGame saved!')
