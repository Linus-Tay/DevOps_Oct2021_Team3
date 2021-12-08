from buildingPools import *
import unittest


bPool = initBuildingPools()

class testbuildings_improve(unittest.TestCase):

    def testbuildOptions_Invalid(self):
        expected = np.array([('BCH',7),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
            dtype=[('Building','U5'),('Copies','<i4')])

        self.assertCountEqual(deductBPoolCopies(bPool,"BCH"),expected)
        
      
        #self.assertEqual(deductBPoolCopies(bPool,"BCH"),bPool[index]['Copies']-1)
    