import random
import numpy as np
from random import randrange


def initBuildingPools():
    buildingPools = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
            dtype=[('Building','U5'),('Copies','<i4')])
    return buildingPools

# def rollBuilding(bPool):
#     b = bPool[randrange(5)]['Building']
#     return b

def gen_pool():
    return random.randint(0,4)

def deductBPoolCopies(bPool,bName):
    x = np.where(bPool['Building']==bName)
    index = x[0][0]
    bPool[index]['Copies']-=1
    return bPool

def viewRemainingBuilds(bPool):
    print('Buildings\tRemaining\n----------\t----------')
    for i in range(len(bPool)):
        print('{}\t\t{}'.format(bPool['Building'][i],bPool['Copies'][i]))
