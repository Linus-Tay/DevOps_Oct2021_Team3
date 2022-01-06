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
class testbuildings_Inputs(unittest.TestCase):
    # test case for when user tries to give an invalid input
    # such as wrong format, more than 2 letter or number-letter
    def testUserInput_Invalid(self):
        with self.assertRaises(ValueError):
            verifyPosition(sample_map,"1A")
        with self.assertRaises(ValueError):
            verifyPosition(sample_map,"Z1")
        with self.assertRaises(IndexError):
            verifyPosition(sample_map,"1")
        with self.assertRaises(IndexError):
            verifyPosition(sample_map,"")
        
    #test case to validate user's x y input to check if the next input x and y is valid
    def testValidate_ValidInput(self):
        self.assertTrue(verifyPosition(sample_map,"A1"))
    

#this class contains the tests cases mainly regarding to buildings validation
class testbuildings_placeBuilds(unittest.TestCase):
    # test case for when user tries to insert building on the same row but different column
    # such as A1 -> B1 -> C1
    # def testBuild_insertBuildingPass(self):
    #     self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",1),2)
    #     self.assertEqual(insertBuild(sample_map,bPool,"D2","BCH",2),3)
        #self.assertTrue(validateXYInput(sample_map,([4,2],[22,22])))
        #self.assertTrue(validateXYInput(sample_map,([4,4,2],[16,22,22])))
       # self.assertEqual(insertBuild(sample_map,bPool,"C2","BCH",3),4) 
        #self.assertTrue(validateXYInput(sample_map,([2,4,4,2],[16,16,22,22])))
  
    def testBuild_insertBuildingFail(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",3),3)
        self.assertFalse(validateXYInput(sample_map,([6,2],[22,4])))
        self.assertFalse(validateXYInput(sample_map,([2,2],[4,22])))
        self.assertFalse(validateXYInput(sample_map,([2,2],[4,4])))

    def testBuild_insertBuildingPass(self):
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",2),3)
        self.assertTrue(validateXYInput(sample_map,([4,2],[22,22])))
        self.assertTrue(validateXYInput(sample_map,([4,2],[16,22])))
        self.assertTrue(validateXYInput(sample_map,([4,4,2],[10,16,22])))


    # # such as A1 -> A1
    def testExistingBuilding(self):
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",1),2)
        self.assertFalse(validateXYInput(sample_map,([2,2],[22,22])))
        self.assertTrue(checkExistingBuilding(sample_map,2,22))
        self.assertFalse(checkExistingBuilding(sample_map,4,4))
    
    # # # #test case internally for when retrieving building names from the play map
    def test_getBuildName(self):
        self.assertEqual(getBuildName(sample_map,2,22),"BCH")
        self.assertEqual(getBuildName(sample_map,4,4),None)

       
# class for test cases when user tries to build adjacent
class test_Buildings_AdjBuilds(unittest.TestCase):

    # test cases for when user tries to build adjacently
    # on the same row
    # on the same column
    # or on different column and different row
    def test_checkAdjBuild(self):
        self.assertEqual(insertBuild(sample_map,bPool,"C3","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B3","BCH",2),3)
        self.assertTrue(checkAdjBuild(sample_map,6,22))
        self.assertEqual(insertBuild(sample_map,bPool,"D3","BCH",3),4)
        self.assertTrue(checkAdjBuild(sample_map,8,10))
        self.assertEqual(insertBuild(sample_map,bPool,"B4","BCH",4),5)
        self.assertTrue(checkAdjBuild(sample_map,4,10))
    
    def test(self):
        with mock.patch('buildingPools.rollBuilding',side_effect=['Data1']):
            self.assertEqual(buildingPools.rollBuilding(),"Data1")


@mock.patch('builtins.print')
def test_viewRemainingBuilds(self):
    # The actual test
    bPool = np.array([('BCH',8),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
        dtype=[('Building','U5'),('Copies','<i4')])
    print_values = []
    builtins.print = lambda s: print_values.append(s)
    buildingPools.viewRemainingBuilds(bPool)
    assert print_values == ['Buildings\tRemaining\n----------\t----------',
                            'BCH\t\t8', 
                            'FAC\t\t8', 
                            'HSE\t\t8', 
                            'SHP\t\t8', 
                            'HWY\t\t8']


       
# # if __name__ == '__main__':
# #     print(testBuild)
# #     unittest.main()