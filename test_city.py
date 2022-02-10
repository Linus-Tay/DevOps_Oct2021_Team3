
import builtins
from io import StringIO
from multiprocessing import pool
import sys
import unittest
import buildingPools
import city
import testBase
import loadSavedGame
poolList = buildingPools.initBuildingPools('BCH','FAC','HSE','SHP','HWY')


class test_City(unittest.TestCase):
    def test_Load_And_View_City(self):
        playMap = city.loadCity('start.csv')
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        city.viewCity(playMap,poolList)
        assert print_values == ["    A     B     C     D   \t\tBuildings\tRemaining",
                                " +-----+-----+-----+-----+\t\tBCH\t\t8",
                                "1|     |     |     |     |\t\tFAC\t\t8",
                                " +-----+-----+-----+-----+\t\tHSE\t\t8",
                                "2|     |     |     |     |\t\tSHP\t\t8",
                                " +-----+-----+-----+-----+\t\tHWY\t\t8",
                                "3|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "4|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                ]
    def test_View_City_With_Invalid_FIle(self):
        self.assertFalse(city.loadCity('fake.txt'))

    # checks whether city dimension size requested is within or equal to 40 squares 
    # only if returns true then newGrid can be loaded
    def test_ValidCitySize(self):
        # 8 * 5 == 40
        self.assertTrue(city.validCitySize(8,5))
        self.assertTrue(city.validCitySize(1,1))
        self.assertTrue(city.validCitySize(2,20))
        self.assertTrue(city.validCitySize(1,20))

    def test_inValidCitySize(self):
        self.assertFalse(city.validCitySize(9,5))
        self.assertFalse(city.validCitySize(10,10))
        self.assertFalse(city.validCitySize('a',10))
        self.assertFalse(city.validCitySize(1,27))

    def test_viewCity_1(self):
        sample_map = city.newGrid(1,26)
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        city.viewCity(sample_map,poolList)
        assert print_values == ["     A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W     X     Y     Z   \t\tBuildings\tRemaining",
                                "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\t\tBCH\t\t8",
                                " 1|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |\t\tFAC\t\t8",
                                "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\t\tHSE\t\t8",
                                "                                                                                                                                                               \t\tSHP\t\t8",
                                "                                                                                                                                                               \t\tHWY\t\t8",
                                ]

    def test_viewCity_2(self):
        sample_map = city.newGrid(1,10)
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        city.viewCity(sample_map,poolList)
        assert print_values == ["     A     B     C     D     E     F     G     H     I     J   \t\tBuildings\tRemaining",
                                "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\t\tBCH\t\t8",
                                " 1|     |     |     |     |     |     |     |     |     |     |\t\tFAC\t\t8",
                                "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\t\tHSE\t\t8",
                                "                                                               \t\tSHP\t\t8",
                                "                                                               \t\tHWY\t\t8",
                                ]

    def test_viewCity_3(self):
        sample_map = city.newGrid(2,5)
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        city.viewCity(sample_map,poolList)
        assert print_values == ["     A     B     C     D     E   \t\tBuildings\tRemaining",
                                "  +-----+-----+-----+-----+-----+\t\tBCH\t\t8",
                                " 1|     |     |     |     |     |\t\tFAC\t\t8",
                                "  +-----+-----+-----+-----+-----+\t\tHSE\t\t8",
                                " 2|     |     |     |     |     |\t\tSHP\t\t8",
                                "  +-----+-----+-----+-----+-----+\t\tHWY\t\t8",
                                ]

    # checks whether it creates the city map accordingly to the dimension size given by user
    # should return a 2d array list
    # should also include the header + gridlines
    def test_NewGrid_smallest(self):
        #test scenario for 1x1 dimension city size
        expected_city = ["     A   \t\tBuildings\tRemaining",
                         "  +-----+\t\tBCH\t\t8",
                         " 1|     |\t\tFAC\t\t8",
                         "  +-----+\t\tHSE\t\t8",
                         "         \t\tSHP\t\t8",
                         "         \t\tHWY\t\t8"
                            ]

        print_values = []
        builtins.print = lambda s: print_values.append(s)
        map_1 = city.newGrid(1,1)
        city.viewCity(map_1,poolList)
        assert print_values == expected_city

    def test_NewGrid_biggest(self):
        #test scenario for 2x10 dimension city size
        expected_city_2 = ["     A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W     X     Y     Z   \t\tBuildings\tRemaining",
                                "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\t\tBCH\t\t8",
                                " 1|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |\t\tFAC\t\t8",
                                "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\t\tHSE\t\t8",
                                "                                                                                                                                                               \t\tSHP\t\t8",
                                "                                                                                                                                                               \t\tHWY\t\t8",
                                ]
       
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        map_2 = city.newGrid(1,26)
        city.viewCity(map_2,poolList)
        assert print_values == expected_city_2

    
        # test scenario for 10x4 dimension city size
        # for rows > 10, there should be a space added infront of the number
        # so that the displayed numbers will be aligned 
        expected_city_3 = [
                            "     A     B     C     D   \t\tBuildings\tRemaining",
                            "  +-----+-----+-----+-----+\t\tBCH\t\t8",
                            " 1|     |     |     |     |\t\tFAC\t\t8",
                            "  +-----+-----+-----+-----+\t\tHSE\t\t8",
                            " 2|     |     |     |     |\t\tSHP\t\t8",
                            "  +-----+-----+-----+-----+\t\tHWY\t\t8",
                            " 3|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 4|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 5|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 6|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 7|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 8|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 9|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            "10|     |     |     |     |",
                            "  +-----+-----+-----+-----+"
                            ]
        
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        map_3 = city.newGrid(10,4)
        city.viewCity(map_3,poolList)
        assert print_values == expected_city_3
        



    def test_startNewGameDefault(self):
        #successfull start new game
        out = StringIO()
        sys.stdout = out 
        testBase.set_keyboard_input(['0'])  
        #default building settings
        citymap = city.newGrid(4,4)
        city.startNewGame(citymap,poolList)
        output = testBase.get_display_output()
        b1 = output[12]
        b2 = output[13]
        assert output == [
                    "Option 1 - Start New Game",
                    "\n-----------------------Turn 1-----------------------\n",
                    "     A     B     C     D   \t\tBuildings\tRemaining",
                    "  +-----+-----+-----+-----+\t\tBCH\t\t8",
                    " 1|     |     |     |     |\t\tFAC\t\t8",
                    "  +-----+-----+-----+-----+\t\tHSE\t\t8",
                    " 2|     |     |     |     |\t\tSHP\t\t8",
                    "  +-----+-----+-----+-----+\t\tHWY\t\t8",
                    " 3|     |     |     |     |",
                    "  +-----+-----+-----+-----+",
                    " 4|     |     |     |     |",
                    "  +-----+-----+-----+-----+",
                    "[1] Build a" + b1[11:15],
                    "[2] Build a" + b2[11:15],
                    "[3] See Current Score\n",
                    "[4] Save Game",
                    "[0] Exit to main menu",
                    "\nYour Choice? "
                    ]
                    

    def test_startNewGameCustom(self):
        #successfull start new game
        out = StringIO()
        sys.stdout = out 
        testBase.set_keyboard_input(['0'])
        #assuming user set the city size to 6x6
        citymap = city.newGrid(6,6)
        custom_pool = buildingPools.initBuildingPools('FAC','HSE','PRK','MON','HWY')
        city.startNewGame(citymap,custom_pool)
        output = testBase.get_display_output()
        b1 = output[16]
        b2 = output[17]
        assert output == [
                    "Option 1 - Start New Game",
                    "\n-----------------------Turn 1-----------------------\n",
                    "     A     B     C     D     E     F   \t\tBuildings\tRemaining",
                    "  +-----+-----+-----+-----+-----+-----+\t\tFAC\t\t8",
                    " 1|     |     |     |     |     |     |\t\tHSE\t\t8",
                    "  +-----+-----+-----+-----+-----+-----+\t\tPRK\t\t8",
                    " 2|     |     |     |     |     |     |\t\tMON\t\t8",
                    "  +-----+-----+-----+-----+-----+-----+\t\tHWY\t\t8",
                    " 3|     |     |     |     |     |     |",
                    "  +-----+-----+-----+-----+-----+-----+",
                    " 4|     |     |     |     |     |     |",
                    "  +-----+-----+-----+-----+-----+-----+",
                    " 5|     |     |     |     |     |     |",
                    "  +-----+-----+-----+-----+-----+-----+",
                    " 6|     |     |     |     |     |     |",
                    "  +-----+-----+-----+-----+-----+-----+",
                    "[1] Build a" + b1[11:15],
                    "[2] Build a" + b2[11:15],
                    "[3] See Current Score\n",
                    "[4] Save Game",
                    "[0] Exit to main menu",
                    "\nYour Choice? "
                    ]
                
    def test_ChooseCitySize_valid(self):
        out = StringIO()
        sys.stdout = out 
        testBase.set_keyboard_input(['5','5','0'])
        default_citymap = city.newGrid(5,5)
        city.chooseCitySize(default_citymap,poolList)
        output = testBase.get_display_output()
        assert output == [
                        "Choose City size with dimension of row and column\n",
                        "Please enter the number of rows desired: ",
                        "Please enter the number of columns desired: ",
                        "Your city map is now 5x5\n",
                        "     A     B     C     D     E   \t\tBuildings\tRemaining",
                        "  +-----+-----+-----+-----+-----+\t\tBCH\t\t8",
                        " 1|     |     |     |     |     |\t\tFAC\t\t8",
                        "  +-----+-----+-----+-----+-----+\t\tHSE\t\t8",
                        " 2|     |     |     |     |     |\t\tSHP\t\t8",
                        "  +-----+-----+-----+-----+-----+\t\tHWY\t\t8",
                        " 3|     |     |     |     |     |",
                        "  +-----+-----+-----+-----+-----+",
                        " 4|     |     |     |     |     |",
                        "  +-----+-----+-----+-----+-----+",
                        " 5|     |     |     |     |     |",
                        "  +-----+-----+-----+-----+-----+",
                        "\n[1] Re-configure city map",
                        "[0] Return to previous menu\n",
                        "Enter your choice? "
        ]

    def test_ChooseCitySize_InvalidOpt(self):
        out = StringIO()
        sys.stdout = out 
        testBase.set_keyboard_input(['a','5','0','5','5','0'])
        default_citymap = city.newGrid(5,5)
        city.chooseCitySize(default_citymap,poolList)
        output = testBase.get_display_output()
        assert output == [
                        "Choose City size with dimension of row and column\n",
                        "Please enter the number of rows desired: ",
                        "Invalid Input! Please enter a number input!\n",
                        "Please enter the number of rows desired: ",
                        "Please enter the number of columns desired: ",
                        "Invalid size! Please retry with a size of minimum of 1 squares and maximum of 40 squares\n",
                        "Please enter the number of rows desired: ",
                        "Please enter the number of columns desired: ",
                        "Your city map is now 5x5\n",
                        "     A     B     C     D     E   \t\tBuildings\tRemaining",
                        "  +-----+-----+-----+-----+-----+\t\tBCH\t\t8",
                        " 1|     |     |     |     |     |\t\tFAC\t\t8",
                        "  +-----+-----+-----+-----+-----+\t\tHSE\t\t8",
                        " 2|     |     |     |     |     |\t\tSHP\t\t8",
                        "  +-----+-----+-----+-----+-----+\t\tHWY\t\t8",
                        " 3|     |     |     |     |     |",
                        "  +-----+-----+-----+-----+-----+",
                        " 4|     |     |     |     |     |",
                        "  +-----+-----+-----+-----+-----+",
                        " 5|     |     |     |     |     |",
                        "  +-----+-----+-----+-----+-----+",
                        "\n[1] Re-configure city map",
                        "[0] Return to previous menu\n",
                        "Enter your choice? "
        ]
