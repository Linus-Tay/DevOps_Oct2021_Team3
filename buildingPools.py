from asyncio.windows_events import NULL
import numpy as np
from random import randrange

def initBuildingPools(b1,b2,b3,b4,b5):
    buildingPools = np.array([(b1,8),(b2,8),(b3,8),(b4,8),(b5,8)],
            dtype=[('Building','U5'),('Copies','<i4')])
    return buildingPools

def rollBuilding(bPool):
    b = bPool[randrange(5)]['Building']
    return b

def deductBPoolCopies(bPool,bName):
    x = np.where(bPool['Building']==bName)
    index = x[0][0]
    bPool[index]['Copies']-=1
    return bPool


def chooseBuildingPools():
    buildingList = [('Beach','BCH'),('Factory','FAC'),('House','HSE'),('Shop','SHP'),('Highway','HWY'),
                    ('Monuments','MON'),('Parks','PRK')]
    chosen_list = []
    counter = 1 
    print("Choose your buildings")
    while counter < 6:
        print("Available Buildings:\n")    
        for x in buildingList:
            # shows building list index (+1) since it starts from 0
            print("[{}] {} ({})".format((buildingList.index(x)+1),x[0],x[1]))

        try:
            b_idx = int(input("\nPlease choose your building (number) from the given options:"))  
            chosen = buildingList[b_idx-1][1]
        except IndexError:
            print("Invalid option, please retry with the options given")
        except ValueError:
            print('Invalid input given, please retry with the options given')
        
        else:        
            #appends chosen building to chosen_list
            chosen_list.append(chosen)
            #removes the chosen building from buildingList
            buildingList.remove(buildingList[b_idx-1])
            if counter < 5:
                print("Your current list: ({})".format(",".join(chosen_list)))
            else:
                print("Your final list: ({})".format(",".join(chosen_list)))
            counter +=1
                   
    return chosen_list




