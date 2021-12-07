from random import sample
import unittest
from Buildings import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


sample_map = loadCity('start.csv')
bPool = initBuildingPools()


class testbuildings_Inputs(unittest.TestCase):
    # test case for when user tries to give an invalid input
    def testUserInput_Invalid(self):
        self.assertEqual(verifyPosition(sample_map,"1A"),(None))
        self.assertEqual(verifyPosition(sample_map,"1A12"),(None)) 
        self.assertEqual(verifyPosition(sample_map,"Z1"),(None))
        
    def testValidate_ValidInput(self):
        self.assertEqual(validateXYInput(sample_map,([2,2],[10,4])),True)
        self.assertEqual(validateXYInput(sample_map,([2,2,2],[16,10,4])),True)
        self.assertEqual(validateXYInput(sample_map,([2,2,2,2],[22,16,10,4])),True)
        self.assertEqual(validateXYInput(sample_map,([4,2],[4,4])),True)
        self.assertEqual(validateXYInput(sample_map,([6,4,2],[4,4,4])),True)
        self.assertEqual(validateXYInput(sample_map,([8,6,4,2],[4,4,4,4])),True)

    #test invalid inputs and if diagonal inputs
    def testValidate_InvalidInput(self):
        self.assertEqual(validateXYInput(sample_map,([6,2],[4,4])),False)
        self.assertEqual(validateXYInput(sample_map,([8,2],[4,4])),False)
        self.assertEqual(validateXYInput(sample_map,([2,2],[16,4])),False)
        self.assertEqual(validateXYInput(sample_map,([2,2],[22,4])),False)
        self.assertEqual(validateXYInput(sample_map,([8,2],[22,4])),False)
        self.assertEqual(validateXYInput(sample_map,([2,2],[4,4])),False)


    def testValidate_DiagonalInput(self):
        self.assertEqual(validateXYInput(sample_map,([2,4],[4,10])),False)
        self.assertEqual(validateXYInput(sample_map,([2,4],[16,10])),False)
        self.assertEqual(validateXYInput(sample_map,([8,4],[4,10])),False)
        self.assertEqual(validateXYInput(sample_map,([8,4],[16,10])),False)
    

class testbuildings_placeBuilds(unittest.TestCase):
    def testBuild_SameRow(self):
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",4),5)

    def testBuild_SameCol(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A3","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"A4","BCH",3),4)

    def testBuild_InvalidBuild(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B4","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C3","BCH",2),2)

    def testExistingBuilding(self):
        self.assertEqual(checkExistingBuilding(sample_map,6,10),False)
        self.assertEqual(checkExistingBuilding(sample_map,2,10),True)
    
    def test_getBuildName(self):
        self.assertEqual(getBuildName(sample_map,2,22),"BCH")
        self.assertEqual(getBuildName(sample_map,6,10),None)

       
        
class test_Buildings_AdjBuilds(unittest.TestCase):
    def test_checkAdjBuild(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C2","BCH",2),3)
        # normal adjacent build
        self.assertEqual(validateXYInput(sample_map,([6,4,4],[16,16,10])),True)

        #same row adjacent build
        self.assertEqual(validateXYInput(sample_map,([4,4,4],[4,16,10])),True)
        self.assertEqual(validateXYInput(sample_map,([4,4,4],[22,16,10])),True)
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"D2","BCH",4),5)

        #different col different row adjacent build
        self.assertEqual(validateXYInput(sample_map,([2,4,4,4,4],[4,22,4,16,10])),True)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",5),6)
        self.assertEqual(validateXYInput(sample_map,([6,4,4,4,4],[22,22,4,16,10])),True)
        self.assertEqual(insertBuild(sample_map,bPool,"D3","BCH",6),7)

        #same col adjacent build
        self.assertEqual(validateXYInput(sample_map,([2,6,2,4,4,4,4],[22,22,4,22,4,16,10])),True)

       


    

    

# if __name__ == '__main__':
#     unittest.main()