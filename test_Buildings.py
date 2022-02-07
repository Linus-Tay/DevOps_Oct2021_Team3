from random import sample
import unittest
from unittest import mock
from buildings import *
import warnings
from city import loadCity
warnings.simplefilter(action='ignore', category=FutureWarning)
import buildingPools
import numpy as np
import builtins
import unittest.mock
sample_map = loadCity('start.csv')
bPool = initBuildingPools()
x = np.where(bPool['Building']=="BCH")
index = x[0][0]
testBuild = bPool[index]

#this class contains the tests cases mainly regarding to inputs validation
class test_UserInputs(unittest.TestCase):
    # test case for when user tries to give an invalid input
    # such as wrong format, more than 2 letter or number-letter
    def test_InvalidUserInput(self):
        self.assertFalse(verifyPosition(sample_map,"11"))
        self.assertFalse(verifyPosition(sample_map,""))
        self.assertFalse(verifyPosition(sample_map,"aaaa"))
        self.assertFalse(verifyPosition(sample_map,"1a"))
        self.assertFalse(verifyPosition(sample_map,"B7"))

    #when user gives an valid letter-number input
    def test_ValidUserInput(self):
        self.assertTrue(verifyPosition(sample_map,"A1"))
        self.assertTrue(verifyPosition(sample_map,"b4"))


#this class contains the tests cases mainly regarding to buildings validation
class test_BuildingPositions(unittest.TestCase):
    
    #when user insert a valid position (first turn)
    def test_ValidPosition(self):
        sample_map[4][10-1] = "B"
        sample_map[4][10] = "C"
        sample_map[4][10+1] = "H"
        self.assertTrue(validatePosition(sample_map,6,10))
    
    #when user insert after first turn 
    def test_InsertAfter1stTurn(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",2),3)
        self.assertTrue(validatePosition(sample_map,2,16))
    
    #when user tries to insert on an exisiting building
    def test_ExistingPosition(self):
        sample_map[4][10-1] = "B"
        sample_map[4][10] = "C"
        sample_map[4][10+1] = "H"
        self.assertFalse(validatePosition(sample_map,4,10))
    
    #when user gave an invalid input (not adjacent to any existing building)
    def test_InvalidPosition(self):
        sample_map[4][10-1] = "B"
        sample_map[4][10] = "C"
        sample_map[4][10+1] = "H"
        self.assertFalse(validatePosition(sample_map,8,10))


#class contains the test cases of inserting buildings
class test_InsertBuildings(unittest.TestCase):

    #when user sucessfully insert a building, turn should increase by 1
    def test_ValidInsert(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"A3","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"B3","BCH",4),5)

     #when inserting building failed due to whatever reasons, turn should remain the same
    def test_InvalidInsert(self):
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"D4","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A4","BCH",2),2)
    
    def test(self):
        with mock.patch('buildingPools.rollBuilding',side_effect=['Data1']):
            self.assertEqual(buildingPools.rollBuilding(),"Data1")


       
# # if __name__ == '__main__':
# #     print(testBuild)
# #     unittest.main()