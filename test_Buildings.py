from random import sample
import pytest
import unittest
from Buildings import *


sample_map = loadCity('start.csv')
bPool = initBuildingPools()


class testbuildings_improve(unittest.TestCase):

    def testInsertBuild(self):
        self.assertEqual(insertBuild(sample_map,bPool,"A1","BCH",1),2)
        self.assertEqual(insertBuild(sample_map,bPool,"B1","BCH",2),3)
        self.assertEqual(insertBuild(sample_map,bPool,"C1","BCH",3),4)
        self.assertEqual(insertBuild(sample_map,bPool,"C2","BCH",4),5)
        self.assertEqual(insertBuild(sample_map,bPool,"A2","BCH",5),6)
        self.assertEqual(insertBuild(sample_map,bPool,"D2","BCH",6),7)

    def testUserInput_invalid(self):
        self.assertEqual(insertRowCol(sample_map,"1A"),(None))

