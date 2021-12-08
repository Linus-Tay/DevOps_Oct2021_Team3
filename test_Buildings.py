from random import sample
import unittest
from Buildings import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


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
        self.assertEqual(verifyPosition(sample_map,"1A"),(None))
        self.assertEqual(verifyPosition(sample_map,"1A12"),(None)) 
        self.assertEqual(verifyPosition(sample_map,"Z1"),(None))
        
    #test case to validate user's x y input to check if the next input x and y is valid
    def testValidate_ValidInput(self):
        self.assertTrue(validateXYInput(sample_map,([2,2],[10,4])))
        self.assertTrue(validateXYInput(sample_map,([2,2,2],[16,10,4])))
        self.assertTrue(validateXYInput(sample_map,([2,2,2,2],[22,16,10,4])))

    #test case for when user tries to input an invalid input
    # invalid such as A1 -> D4 
    def testValidate_InvalidInput(self):
        self.assertFalse(validateXYInput(sample_map,([6,2],[4,4])))
        self.assertFalse(validateXYInput(sample_map,([8,2],[4,4])))
        self.assertFalse(validateXYInput(sample_map,([2,2],[4,4])))

    #test case for when user tries to input a diagonal input
    # such as C3 -> B2 or A4 -> B3
    def testValidate_DiagonalInput(self):
        self.assertFalse(validateXYInput(sample_map,([2,4],[4,10])))
        self.assertFalse(validateXYInput(sample_map,([6,4],[4,10])))
       
    

#this class contains the tests cases mainly regarding to buildings validation

class testbuildings_placeBuilds(unittest.TestCase):

    # test case for when user tries to insert building on the same row but different column
    # such as A1 -> B1 -> C1
    def testBuild_SameRow(self):
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",4),5)


    #test case for when user tries to insert building on the same column but different row
    # # such as A1 -> A2 -> A3 -> A4
    def testBuild_SameCol(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A3","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"A4","BCH",3),4)

    #test case for when user tries to insert an invalid building
    # # such as A1 -> A4 or D4 -> D1 or B2 -> A4
    def testBuild_InvalidBuild(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B4","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",2),2)
    

    #test case for when user tries to insert on an existing building
    # such as A1 -> A1
    def testExistingBuilding(self):
        self.assertFalse(checkExistingBuilding(sample_map,6,10))
        self.assertTrue(checkExistingBuilding(sample_map,2,10))
    
    # #test case internally for when retrieving building names from the play map
    def test_getBuildName(self):
        self.assertEqual(getBuildName(sample_map,2,22),"BCH")
        self.assertEqual(getBuildName(sample_map,6,10),None)

       
# class for test cases when user tries to build adjacent
class test_Buildings_AdjBuilds(unittest.TestCase):

#     #test cases for when user tries to build adjacently
#     # on the same row
#     # on the same column
#     # or on different column and different row
    def test_checkAdjBuild(self):
        # test adjacent build
        # adjacent function has to depends on validate function in order to be executed
        # hence here is testing validate and insert build to check for adjacent build
        self.assertEqual(insertBuild(sample_map,bPool,"C3","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"D3","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"C4","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"C2","BCH",4),5)
        self.assertEqual(insertBuild(sample_map,bPool,"D4","BCH",5),6)
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",6),7)
        #same row adjacent
        self.assertTrue(validateXYInput(sample_map,([8,8,8],[10,22,16])))
        self.assertTrue(validateXYInput(sample_map,([6,8,8],[16,22,16])))
        # #different col different row adjacent build
        self.assertTrue(validateXYInput(sample_map,([8,6,8,8],[10,16,22,16])))


       
if __name__ == '__main__':
    print(testBuild)
    unittest.main()