import numpy as np
from random import randrange

def initBuildingPools():
    buildingPools = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
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

    opt = 0
    updated = False
    print("Choose your buildings")
    while opt == 0 and updated != True:
        print("Available Buildings:\n")
        for builds in buildingList:
            # shows building list index (+1) since it starts from 0
            print("[{}] {} ({})".format(buildingList.index(builds)+1,builds[0],builds[1]))
        
        try:
            b_idx = int(input("\nPlease choose your building (number) from the given options: "))
        except ValueError:
            print('Invalid input given, please retry with the options given')
        else:
            if b_idx == 0:
                print("Invalid option, please retry with the options given")
            else: 
                try:
                    chosen = buildingList[b_idx-1][1]
                except IndexError:
                    print("Invalid option, please retry with the options given")
                else:
                    #appends chosen building into current list
                    chosen_list.append(chosen)
                    #remove chosen building from available list
                    buildingList.remove(buildingList[b_idx-1])
                    if len(chosen_list) < 5:
                        print("Your current list: ({})".format(",".join(chosen_list)))
                    elif len(chosen_list) == 5:
                        print("Your final list: ({})".format(",".join(chosen_list)))
                        updated = True

                        print("\n[1] Re-configure city map")
                        print("[0] Return to previous menu\n")
                        option = int(input("Enter your choice? "))

                        if option == 1:
                            #reset if user wants to re-configure
                            buildingList = [('Beach','BCH'),('Factory','FAC'),('House','HSE'),('Shop','SHP'),('Highway','HWY'),
                                            ('Monuments','MON'),('Parks','PRK')]
                            chosen_list = []
                            updated = False
                        else:
                            return chosen_list