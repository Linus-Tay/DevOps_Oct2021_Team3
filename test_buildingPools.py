import unittest
import buildingPools
import numpy as np
import builtins
import unittest.mock
from random import Random
from unittest.mock import patch

bPool = buildingPools.initBuildingPools()
random = Random()

class testbuildings_improve(unittest.TestCase):

    def testbuildOptions_Invalid(self):
        expected = np.array([('BCH',7),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
            dtype=[('Building','U5'),('Copies','<i4')])

        self.assertCountEqual(buildingPools.deductBPoolCopies(bPool,"BCH"),expected)

    def test_generate_rand(self):
        self.assertTrue(buildingPools.gen_pool() <= 4 and buildingPools.gen_pool() >=0)


def test_viewRemainingBuilds():
    # The actual test
    with unittest.mock.patch('builtins.print'):
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

# def setUp(self):
#     self.random = Random(5)

    
# def test_gen_pool():
#     with unittest.mock.patch('package.file.random'):
#         random.randint._mock_side_effect = random.randit
#         assert random == buildingPools.gen_pool()
#         #self.assertEqual(buildingPools.gen_pool(),3)
        