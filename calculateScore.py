# GameOption 4 - View Current Score
from distutils.command.build import build
from itertools import tee, islice, chain
# https://stackoverflow.com/questions/1011938/loop-that-also-accesses-previous-and-next-values

# This Function gets the previous and next item from the selected item in an array
def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def calculateScore(playCity,dimension):
    # Change Dimension to string
    dimension[0] = str(dimension[0])
    dimension[-1] = str(dimension[-1])

    dict = mapBuildingsToCords(playCity)
   
   # Calculate HSE
    HSEScore = calculateHSE(dict)

   # Calculate FAC
    FACScore = calculateFAC(dict)

    # Calculate SHP
    SHPScore = calculateSHP(dict)
    
    # Calculate HWY
    HWPScore = calculateHWY(dict)

    # Calculate BCH
    BCHScore = calculateBCH(dict,playCity,dimension)

    totalScore = BCHScore + FACScore + HSEScore + SHPScore + HWPScore
    print("\nTotal Score: "+ str(totalScore))

    return totalScore
    
def mapBuildingsToCords(playCity):
    # Create Dictionary 
    dict = {}
    col = 2
    row = 3
    AlphaNum = 4
    while row < (len(playCity[0])-1):
        rowNumCount = 1
        while col < (len(playCity)-1):
            colAlpha = playCity[0][AlphaNum]
            building = str(playCity[col][row])+str(playCity[col][row+1])+str(playCity[col][row+2])
            if building == '   ':
                dict["{}{}".format(colAlpha,rowNumCount)] = None
            else:
                dict["{}{}".format(colAlpha,rowNumCount)] = building
            rowNumCount +=1
            col +=2
        AlphaNum += 6
        row += 6
        col = 2
    return(dict)

def calculateBCH(dict,playCity,dimension):
    i = 0
    BCHCount = 0
    rowNumCount = 1
    lastalph = alist[int(dimension[-1])-1]

    while i < int(dimension[0]):
        # Check if BCH 
        # check if dimension is [*,1]
        if dimension[-1] == "1":
            if str(dict.get("A{}".format(rowNumCount))) == "BCH":
                BCHCount += 1
        else:
            if str(dict.get("A{}".format(rowNumCount))) == "BCH":
                BCHCount += 1
            if str(dict.get("{}{}".format(lastalph,rowNumCount))) == "BCH":
                BCHCount += 1
        i += 1
        rowNumCount += 1
    
    if BCHCount == 0:
        print("BCH: 0 ")
        return 0
    else:
        stmt = ""
        num=1
        while num <= BCHCount:
            if num == BCHCount:
                stmt+= "3"
            else:
                stmt+= "3 + "
            num +=1
        subScore = 3*BCHCount
        print("BCH: " + stmt + " = " + str(subScore))
        return subScore

def calculateFAC(dict):
    FACCount = 0
    # Get all FAC buildings
    for building in dict.values():
        if building == "FAC":
            FACCount +=1
    # Craft Statement
    stmt = ""
    # If no FAC
    if FACCount == 0:
        print("FAC: 0")
        return 0
    else:
        # IF there is 4 or more FAC
        if FACCount >= 4:
            stmt += "4 + 4 + 4 + 4"
            FACCount -= 4
            num=1
            # Subsequenct FAC is 1 point
            while num <= FACCount:
                stmt+=" + 1"
                num +=1
            subScore = (4*4)+(num-1)
            print("FAC: " + stmt + " = " + str(subScore))
        else: # There is less than 4 FAC
            num=1
            while num <= FACCount:
                if num == FACCount:
                    stmt+= "{}".format(FACCount)
                else:
                    stmt+= "{} + ".format(FACCount)
                num +=1
            subScore = FACCount*FACCount
            print("FAC: " + stmt + " = " + str(subScore))
        return subScore

def calculateHSE(dict):
    stmt = ""
    totalScore = 0
    HSECount = 0
    # print(dict.items())
    for item in dict.items():
        if item[1] == "HSE":
            subScore = 0
            # Check building around HSE if its FAC
            up = getUpwwardsBuilding(dict,item[0])
            down = getDownwardsBuilding(dict,item[0])
            left = getLeftBuilding(dict,item[0])
            right = getRightBuilding(dict,item[0])
            if right == None:
                right = None
            else:
                right = right[-1]
            if left == None:
                left = None
            else:
                left = left[-1]
            if down == None:
                down = None
            else:
                down = down[-1]
            if up == None:
                up = None
            else:
                up = up[-1]
            if up == "FAC" or down == "FAC" or left == "FAC" or right == "FAC":
                subScore +=1
            else:
                if up == "HSE" or up == "SHP":
                    subScore += 1
                if down == "HSE" or down == "SHP":
                    subScore += 1
                if left == "HSE" or left == "SHP":
                    subScore += 1
                if right == "HSE" or right == "SHP":
                    subScore += 1
                if up == "BCH":
                    subScore += 2
                if down == "BCH":
                    subScore += 2
                if left == "BCH":
                    subScore += 2
                if right == "BCH":
                    subScore += 2
            totalScore += subScore
            if HSECount == 0:
                stmt += str(subScore)
            else:
                stmt += " + {}".format(subScore)
            HSECount += 1
    if HSECount == 0:
        print("HSE: {}".format(totalScore))
    else:
        print("HSE: {} = {}".format(stmt,totalScore))
    return totalScore

def calculateSHP(dict):
    stmt = ""
    SHPCount = 0 
    totalScore = 0
    for item in dict.items():
        if item[1] == "SHP":
            subScore = 0
            # Check building around SHP
            up = getUpwwardsBuilding(dict,item[0])
            down = getDownwardsBuilding(dict,item[0])
            left = getLeftBuilding(dict,item[0])
            right = getRightBuilding(dict,item[0])
            if right == None:
                right = None
            else:
                right = right[-1]
            if left == None:
                left = None
            else:
                left = left[-1]
            if down == None:
                down = None
            else:
                down = down[-1]
            if up == None:
                up = None
            else:
                up = up[-1]
            list = [up,down,left,right]
            res = []
            for i in list:
                if i not in res:
                    if i == None:
                        pass
                    else:
                        res.append(i)
            subScore += len(res)
            if SHPCount == 0:
                stmt += str(len(res))
            else:
                stmt += " + {}".format(len(res))
            totalScore += subScore
            SHPCount += 1
    if SHPCount == 0:
        print("SHP: 0")
        return 0
    else:
        print("SHP: {} = {}".format(stmt, totalScore))
        return totalScore

def calculateHWY(dict):
    stmt = ""
    num = 0
    HWYCount = 0 
    totalScore = 0
    for item in dict.items():
        # Check if Item is Park
        if item[1] == "HWY":
            subScore = 1
            # Get Coordinates of building
            cords = item[0]
            while True :
                left = getLeftBuilding(dict,cords)
                if left == None or left[-1] != "HWY":
                    break
                else: 
                    cords = left[0]
                    subScore += 1
            # Set coords back to item HWY
            cords = item[0]
            while True :
                right = getRightBuilding(dict,cords)
                if right == None or right[-1] != "HWY":
                    break
                else: 
                    cords = right[0]
                    subScore += 1
            if subScore>1: 
                totalScore += subScore
            else:
                totalScore += 1
                subScore = 1
            if num == 0:
                stmt += "{}".format(subScore)
                num += 1
            else:
                stmt += " + {}".format(subScore)
                num += 1
            HWYCount += 1
    if HWYCount == 0:
        print("HWY: 0")
        return 0
    else:
        print("HWY: {} = {}".format(stmt,totalScore))    
        return totalScore
  
def getLeftBuilding(dict,cord):
    # print("dict",dict)
    # print("cord",cord)
    for previous, item, next in previous_and_next(alist):
        if cord[0] == item:
            if previous == None:
                return None
            else:
                left = str(previous) + str(cord[1])
                break
    building = dict.get(left)
    leftList = [left,building]
    return leftList

def getRightBuilding(dict,cord):
    for previous, item, next in previous_and_next(alist):
        if cord[0] == item:
            if next == None:
                return None
            else:
                right = str(next) + cord[1]
                break
    building = dict.get(right)
    rightList = [right,building]
    return rightList

def getUpwwardsBuilding(dict,cord):
    up = cord[0] + str(int(cord[-1]) - 1)
    building = dict.get(up)
    upList = [up,building]
    return upList

def getDownwardsBuilding(dict,cord):
    down = cord[0] + str(int(cord[-1]) + 1)
    building = dict.get(down)
    downList = [down,building]
    return downList

def getPRKs(dict):
    PRKAccounted = []
    for item in dict.items():
        # Check if item is PRK
        if item[1] == "PRK":
            cords = item[0]
            tempList = []
            tempList.append(cords)
            # Count how many parks upwards and add to subscore
            up = getUpwwardsBuilding(dict,cords)
            # print(right,"right")
            if up != None and up[-1] == "PRK":
                tempList.append(up[0])
            # # Count how many parks downwards and add to subscore
            down = getDownwardsBuilding(dict,cords)
                # print(right,"right")
            if down != None and down[-1] == "PRK":
                tempList.append(down[0])
            # Count how many parks on the left and add to subscore
            left = getLeftBuilding(dict,cords)
            if left != None and left[-1] == "PRK":
                tempList.append(left[0])
            # Count how many parks on the right and add to subscore
            right = getRightBuilding(dict,cords)
            if right != None and right[-1] == "PRK":
                tempList.append(right[0])

            # print(tempList,"TEMP")
            if len(PRKAccounted) == 0:
                # If prkaccounted is empty just add list
                PRKAccounted.append(tempList)
            else:
                # Get individual array in prkaccounted
                for i in range(len(PRKAccounted)):
                    # Set counter for cordz in templist to 1
                    count = 1
                    for cordz in tempList:
                        # Check if cordz in temp list is inside individual array 
                        if cordz in PRKAccounted[i]:
                            # If yes, add cordz not inside into individual array
                            for item in tempList:
                                if not item in PRKAccounted[i]:
                                    PRKAccounted[i].append(item)
                        # Else if cordz in temp list not inside individual array
                        # Check if all cordz in temp list has been checked using counter
                        elif count == len(tempList):
                            # if no cordz in temp list is not inside the individual park accounted list
                            # check if he have check all park accounted list
                            # If yes, add templist to Park accounted list as a new array (New Group)
                            if (i+1) == len(PRKAccounted): 
                                PRKAccounted.append(tempList)
                            # Else, pass first
                            else:
                                pass
                        count +=1
    # print(PRKAccounted, "HEY")
    return PRKAccounted

def calculatePRK(dict):
    stmt = ""
    num = 0
    PRKAccounted = []
    PRKCountList = []
    totalScore = 0
    count = 1
    PRKList = getPRKs(dict)
    if len(PRKList) == 0:
        print("PRK: 0")
        return 0
    else:
        for item in PRKList:
            if count == len(PRKList):
                if len(item) == 1:
                    totalScore += 1
                    stmt += "1"
                elif len(item) == 2:
                    totalScore += 3
                    stmt += "3"
                elif len(item) == 3:
                    totalScore +=  8
                    stmt += "8"
                elif len(item) == 4:
                    totalScore += 16
                    stmt += "16"
                elif len(item) == 5:
                    totalScore += 22 
                    stmt += "22"
                elif len(item) == 6:
                    totalScore += 23
                    stmt += "23"
                elif len(item) == 7:
                    totalScore += 24  
                    stmt += "24"
                elif len(item) == 8:
                    totalScore += 25
                    stmt += "25"
            else:
                if len(item) == 1:
                    totalScore += 1
                    stmt += "1"
                elif len(item) == 2:
                    totalScore += 3
                    stmt += "3"
                elif len(item) == 3:
                    totalScore +=  8
                    stmt += "8"
                elif len(item) == 4:
                    totalScore += 16
                    stmt += "16"
                elif len(item) == 5:
                    totalScore += 22 
                    stmt += "22"
                elif len(item) == 6:
                    totalScore += 23
                    stmt += "23"
                elif len(item) == 7:
                    totalScore += 24  
                    stmt += "24"
                elif len(item) == 8:
                    totalScore += 25
                    stmt += "25"
                stmt += " + "
                count += 1
            
        print("PRK: {} = {}".format(stmt,totalScore))
        return totalScore

def calculateMON(dict,dimension):
    # Using dimension get the A1, last aplha 1, last alpha last row, a last row
    if dimension[-1] == "1":
        # Only 2 sides eg. ["A1", "A4"] 
        corners = ["A1", "A" + dimension[0]]
    elif dimension[0] == "1":
        # Only 2 sides eg. ["A1", "D1"] 
        corners = ["A1", alist[int(dimension[-1])-1] + "1"]
    else:
        # 4 sides eg. ["A1", "A4", "D1", "D4"] 
        corners = ["A1",
                    "A" + dimension[0],
                    alist[int(dimension[-1])-1] + "1",
                    alist[int(dimension[-1])-1] + dimension[0]]
    monCoords = []
    scoreStatementList = []
    for item in dict.items():
        if item[1] == "MON":
            monCoords.append(item[0])
    if len(monCoords) >= 3:
        score = len(monCoords) * 4
        for i in range(len(monCoords)):
            scoreStatementList.append("4")
    else:
        score = 0
        count = 1
        for item in monCoords:
            for side in corners:
                if item == side:
                    score += 2
                    scoreStatementList.append("2")
                    break
                # elif by the end of the last side in corners, 
                # and the item is not a side, add 1 to score
                elif count == len(corners): 
                    score += 1
                    scoreStatementList.append("1")
                count += 1
    if score == 0:
        print("MON: 0")
        return 0
    else:
        scoreStatement = "MON: "
        count = 1
        for i in scoreStatementList:
            if count == len(scoreStatementList):
                scoreStatement += "{}".format(i)
            else:
                scoreStatement += "{} + ".format(i)
            count += 1
        print(scoreStatement + " = " + str(score))
        return score

# Alphabet list (First 20 Alplhabet)
alist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

