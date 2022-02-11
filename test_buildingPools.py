import unittest
import buildingPools
import numpy as np
import builtins
import unittest.mock
import buildingPools
import testBase

class testbuildings_improve(unittest.TestCase):

    def testbuildOptions_Invalid(self):
        expected = np.array([('BCH',7),('FAC',8),('HSE',8),('SHP',8),('HWY',8)],
            dtype=[('Building','U5'),('Copies','<i4')])
        bPool = buildingPools.initBuildingPools('BCH','FAC','HSE','SHP','HWY')
        self.assertCountEqual(buildingPools.deductBPoolCopies(bPool,"BCH"),expected)

        #self.assertEqual(deductBPoolCopies(bPool,"BCH"),bPool[index]['Copies']-1)
    
    def test_InitBuildingPool(self):
        expected_1 = np.array([('BCH',8),('PRK',8),('MON',8),('SHP',8),('HWY',8)],
                                dtype=[('Building','U5'),('Copies','<i4')])
        initPool = buildingPools.initBuildingPools('BCH','PRK','MON','SHP','HWY')
        assert (expected_1 == initPool).all()

    def test_ChooseBuildingPoolList(self):
        testBase.set_keyboard_input(['7','5','1','3','2','0'])
        expected_pool = np.array([('PRK',8),('HWY',8),('BCH',8),('SHP',8),('HSE',8)],
            dtype=[('Building','U5'),('Copies','<i4')])
        chosenPools = buildingPools.chooseBuildingPools()
        output = testBase.get_display_output()
        assert output == [
                        "Choose your buildings",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "[7] Parks (PRK)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK)",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK,HWY)",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK,HWY,BCH)",
                        "Available Buildings:\n",
                        "[1] Factory (FAC)",
                        "[2] House (HSE)",
                        "[3] Shop (SHP)",
                        "[4] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK,HWY,BCH,SHP)",
                        "Available Buildings:\n",
                        "[1] Factory (FAC)",
                        "[2] House (HSE)",
                        "[3] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your final list: (PRK,HWY,BCH,SHP,HSE)",
                        "\n[1] Re-configure city map",
                        "[0] Return to previous menu\n",
                        "Enter your choice? " 
                    ]
        # initiate building pool from the list choose building pool return             
        final_pool = buildingPools.initBuildingPools(chosenPools[0],chosenPools[1],chosenPools[2],chosenPools[3],chosenPools[4])
        assert(final_pool==expected_pool).all()

    def test_ChooseBuildingPool_InvalidInputs(self):
        testBase.set_keyboard_input(['0','','a','10','7','5','1','3','2','0','0'])

        chosenPools = buildingPools.chooseBuildingPools()
        output = testBase.get_display_output()
        assert output == [
                        "Choose your buildings",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "[7] Parks (PRK)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Invalid option, please retry with the options given",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "[7] Parks (PRK)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Invalid input given, please retry with the options given",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "[7] Parks (PRK)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Invalid input given, please retry with the options given",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "[7] Parks (PRK)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Invalid option, please retry with the options given",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "[7] Parks (PRK)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK)",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Highway (HWY)",
                        "[6] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK,HWY)",
                        "Available Buildings:\n",
                        "[1] Beach (BCH)",
                        "[2] Factory (FAC)",
                        "[3] House (HSE)",
                        "[4] Shop (SHP)",
                        "[5] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK,HWY,BCH)",
                        "Available Buildings:\n",
                        "[1] Factory (FAC)",
                        "[2] House (HSE)",
                        "[3] Shop (SHP)",
                        "[4] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your current list: (PRK,HWY,BCH,SHP)",
                        "Available Buildings:\n",
                        "[1] Factory (FAC)",
                        "[2] House (HSE)",
                        "[3] Monuments (MON)",
                        "\nPlease choose your building (number) from the given options: ",
                        "Your final list: (PRK,HWY,BCH,SHP,HSE)",
                        "\n[1] Re-configure city map",
                        "[0] Return to previous menu\n",
                        "Enter your choice? "      
                    ]
