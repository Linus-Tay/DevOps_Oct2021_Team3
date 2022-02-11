from random import sample
import unittest
from unittest import mock
from buildings import *
import warnings
import city 
warnings.simplefilter(action='ignore', category=FutureWarning)
import buildingPools
import numpy as np
import builtins
import unittest.mock
import main
bPool = buildingPools.initBuildingPools('BCH','FAC','HSE','SHP','HWY')
map_4x4 = city.newGrid(4,4)
map_4x10 = city.newGrid(4,10)
map_6x6 = city.newGrid(6,6)
#this class contains the tests cases mainly regarding to inputs validation
class test_UserInputs(unittest.TestCase):
    
    # test case for when user tries to give an invalid input
    # such as wrong format, more than 2 letter or number-letter
    def test_InvalidUserInput(self):
        self.assertFalse(validatePosition(map_4x4,"11"))
        self.assertFalse(validatePosition(map_4x4,""))
        self.assertFalse(validatePosition(map_4x4,"aaaa"))
        self.assertFalse(validatePosition(map_4x4,"1a"))
    

    #when user gives an valid letter-number input
    def test_ValidUserInput_4x4(self):
        self.assertTrue(validatePosition(map_4x4,"A1"))
        self.assertTrue(validatePosition(map_4x4,"b4"))

    #when citymap is 4x10
    def test_ValidUserInput_4x10(self):
        self.assertTrue(validatePosition(map_4x10,"J4"))
        self.assertTrue(validatePosition(map_4x10,"F1"))
    
    #when city map is 6x6
    def test_ValidUserInput_6x6(self):
        main.dimension = [6,6]
        self.assertTrue(validatePosition(map_6x6,"E6"))
        self.assertTrue(validatePosition(map_6x6,"D5"))



#this class contains the tests cases mainly regarding to buildings validation
class test_BuildingPositions(unittest.TestCase):
     #insert fake building in "B2" in a map size of 4x4
    map_4x4[4][10-1] = "B"
    map_4x4[4][10] = "C"
    map_4x4[4][10+1] = "H"

    #insert fake building in "J1" in a map size of 4x10
    map_4x10[2][58-1] = "B"
    map_4x10[2][58] = "C"
    map_4x10[2][58+1] = "H"
    
    #when user insert a valid position (first turn) in position "C3"
    def test_ValidPosition_4x4(self):
        self.assertTrue(verifyPosition(map_4x4,6,10))

    #when user insert a valid position (first turn) in position "J3"
    def test_ValidPosition_4x10(self):
        self.assertTrue(verifyPosition(map_4x10,6,58))

    #when user insert after first turn 
    def test_InsertAfter1stTurn_4x4(self):
        self.assertEqual(insertBuild(map_4x4,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(map_4x4,bPool,"B1","BCH",2),3)
        self.assertTrue(verifyPosition(map_4x4,2,16))
    
     #when user insert after first turn 
    def test_InsertAfter1stTurn_4x10(self):
        self.assertEqual(insertBuild(map_4x10,bPool,"J4","BCH",1),2)
        self.assertEqual(insertBuild(map_4x10,bPool,"I4","BCH",2),3)
        # Verify the next position if user were to build on "H4"
        self.assertTrue(verifyPosition(map_4x10,8,46))
    
    #when user tries to insert on an exisiting building
    def test_NonExistingPosition_4x4(self):
        self.assertFalse(checkExistingBuilding(map_4x4,6,22))

    #when user tries to insert on an exisiting building
    def test_NonExistingPosition_4x10(self):
        self.assertFalse(checkExistingBuilding(map_4x4,2,58))

    #when user tries to insert on an exisiting building
    def test_ExistingPosition_4x10(self):
        self.assertTrue(checkExistingBuilding(map_4x10,2,58))
    
    #when user gave an invalid input (not adjacent to any existing building)
    def test_InvalidPosition_4x4(self):
        self.assertFalse(verifyPosition(map_4x4,8,10))

    def test_InvalidPosition_4x10(self):
        self.assertFalse(verifyPosition(map_4x10,4,10))


#class contains the test cases of inserting buildings
class test_InsertBuildings(unittest.TestCase):

    #when user sucessfully insert a building, turn should increase by 1
    def test_ValidInsert_4x4(self):
        self.assertEqual(insertBuild(map_4x4,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(map_4x4,bPool,"A2","BCH",2),3)
        self.assertEqual(insertBuild(map_4x4,bPool,"A3","BCH",3),4)
        self.assertEqual(insertBuild(map_4x4,bPool,"B3","BCH",4),5)

     #when inserting building failed due to whatever reasons, turn should remain the same
    def test_InvalidInsert_4x4(self):
        self.assertEqual(insertBuild(map_4x4,bPool,"D1","BCH",1),2)
        self.assertEqual(insertBuild(map_4x4,bPool,"D4","BCH",2),2)
        self.assertEqual(insertBuild(map_4x4,bPool,"A4","BCH",2),2)

    
     #when user sucessfully insert a building, turn should increase by 1
    def test_ValidInsert_4x10(self):
        self.assertEqual(insertBuild(map_4x10,bPool,"C1","BCH",1),2)
        self.assertEqual(insertBuild(map_4x10,bPool,"D1","BCH",2),3)
        self.assertEqual(insertBuild(map_4x10,bPool,"E1","BCH",3),4)
        self.assertEqual(insertBuild(map_4x10,bPool,"F1","BCH",4),5)

     #when inserting building failed due to whatever reasons, turn should remain the same
    def test_InvalidInsert_4x10(self):
        self.assertEqual(insertBuild(map_4x10,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(map_4x10,bPool,"D4","BCH",2),2)
        self.assertEqual(insertBuild(map_4x10,bPool,"F4","BCH",2),2)
    
    def test(self):
        with mock.patch('buildingPools.rollBuilding',side_effect=['Data1']):
            self.assertEqual(buildingPools.rollBuilding(),"Data1")

       
# # if __name__ == '__main__':
# #     print(testBuild)
# #     unittest.main()