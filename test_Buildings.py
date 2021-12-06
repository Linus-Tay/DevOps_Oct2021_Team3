from random import sample
import unittest
from Buildings import *


sample_map = loadCity('start.csv')
bPool = initBuildingPools()


class testbuildings_improve(unittest.TestCase):

    def testInsertBuild_DiagonalInput(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A3","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C3","BCH",2),2)

    def testInsertBuild_InvalidInput(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B4","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"D4","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C4","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"D3","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A3","BCH",2),2)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",2),2)
    
    def testSucessBuild(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"B3","BCH",4),5)
        self.assertEqual(insertBuild(sample_map,bPool,"C3","BCH",5),6)

        
    def testInsertBuild_SameCol(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"A3","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"A4","BCH",4),5)
       
    def testInsertBuild_SameRow(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",4),5)
    
    #test several possible scenario for adjacent buildings
    def testInsertBuildAdjBuild_scenarioA(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",4),5)
        self.assertEqual(insertBuild(sample_map,bPool,"D2","BCH",5),6)
        self.assertEqual(insertBuild(sample_map,bPool,"D3","BCH",6),7)
        self.assertEqual(insertBuild(sample_map,bPool,"D4","BCH",7),8)
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",8),9)
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",9),10)

    def testInsertBuildAdjBuild_scenarioB(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",4),5)
    
    def testInsertBuildAdjBuild_scenarioC(self):
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B2","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"D1","BCH",4),5)
        self.assertEqual(insertBuild(sample_map,bPool,"B3","BCH",5),6)
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",6),7)
    
    
    def testUserInput_invalid(self):
        self.assertEqual(insertRowCol(sample_map,"1A"),(None))

