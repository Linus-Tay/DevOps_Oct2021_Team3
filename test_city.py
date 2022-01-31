
import builtins
from io import StringIO
import sys
import unittest
from buildingPools import initBuildingPools
import city
import main
import testBase


class test_City(unittest.TestCase):
    def test_Load_And_View_City(self):
        playMap = city.loadCity('start.csv')
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        city.viewCity(playMap)
        assert print_values == ["    A     B     C     D   ",
                                " +-----+-----+-----+-----+",
                                "1|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "2|     |     |     |     |",
                                " +-----+-----+-----+-----+",
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

    def test_inValidCitySize(self):
        self.assertFalse(city.validCitySize(9,5))
        self.assertFalse(city.validCitySize(10,10))
        self.assertFalse(city.validCitySize('a',10))




    # checks whether it creates the city map accordingly to the dimension size given by user
    # should return a 2d array list
    # should also include the header + gridlines
    def test_NewGrid_smallest(self):
        #test scenario for 1x1 dimension city size
        expected_city = ["     A   ",
                         "  +-----+",
                         " 1|     |",
                         "  +-----+"
                            ]

        print_values = []
        builtins.print = lambda s: print_values.append(s)
        map_1 = city.newGrid(1,1)
        city.viewCity(map_1)
        assert print_values == expected_city

    def test_NewGrid_biggest(self):

        #test scenario for 2x10 dimension city size
        expected_city_2 = [
                            "     A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W     X     Y     Z   ",
                            "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+",
                            " 1|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |",
                            "  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+"
                            ]
       
        print_values = []
        builtins.print = lambda s: print_values.append(s)
        map_2 = city.newGrid(1,26)
        city.viewCity(map_2)
        assert print_values == expected_city_2

    
        # test scenario for 10x4 dimension city size
        # for rows > 10, there should be a space added infront of the number
        # so that the displayed numbers will be aligned 
        expected_city_3 = [
                            "     A     B     C     D   ",
                            "  +-----+-----+-----+-----+",
                            " 1|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
                            " 2|     |     |     |     |",
                            "  +-----+-----+-----+-----+",
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
        city.viewCity(map_3)
        assert print_values == expected_city_3
        



    def test_startNewGameDefault(self):
        #successfull start new game
        out = StringIO()
        sys.stdout = out 
        #testBase.set_keyboard_input(['1','a','2','0'])
        testBase.set_keyboard_input(['0'])  
        #default building settings
        citymap = city.newGrid(4,4)
        pool = initBuildingPools()
        city.startNewGame(citymap,pool)
        output = testBase.get_display_output()
        b1 = output[12]
        b2 = output[13]
        assert output == [
                    "Option 1 - Start New Game",
                    "\n-----------------------Turn 1-----------------------\n",
                    "     A     B     C     D   ",
                    "  +-----+-----+-----+-----+",
                    " 1|     |     |     |     |",
                    "  +-----+-----+-----+-----+",
                    " 2|     |     |     |     |",
                    "  +-----+-----+-----+-----+",
                    " 3|     |     |     |     |",
                    "  +-----+-----+-----+-----+",
                    " 4|     |     |     |     |",
                    "  +-----+-----+-----+-----+",
                    "[1] Build a" + b1[11:15],
                    "[2] Build a" + b2[11:15],
                    "[3] See remaining buildings",
                    "[4] See Current Score\n",
                    "[5] Save Game",
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
        pool = initBuildingPools()
        city.startNewGame(citymap,pool)
        output = testBase.get_display_output()
        b1 = output[16]
        b2 = output[17]
        assert output == [
                    "Option 1 - Start New Game",
                    "\n-----------------------Turn 1-----------------------\n",
                    "     A     B     C     D     E     F   ",
                    "  +-----+-----+-----+-----+-----+-----+",
                    " 1|     |     |     |     |     |     |",
                    "  +-----+-----+-----+-----+-----+-----+",
                    " 2|     |     |     |     |     |     |",
                    "  +-----+-----+-----+-----+-----+-----+",
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
                    "[3] See remaining buildings",
                    "[4] See Current Score\n",
                    "[5] Save Game",
                    "[0] Exit to main menu",
                    "\nYour Choice? "
                    ]
                    
    def test_startNewGameFail(self):
        # when user enters invalid dimension
        out = StringIO()
        sys.stdout = out 
        testBase.set_keyboard_input(['1','10','5'])
        main.mainMenu()
        output = testBase.get_display_output()
        assert output == [
                    "\nWelcome, mayor of Simp City!",
                    "----------------------------",
                    "[1] Start new game",
                    "[2] Load saved game",
                    "\n[0] Exit",
                    "\nEnter your choice? ",
                    "Option 1 - Start New Game",
                    "Please select city map size in the dimension of row * column\n",
                    "Please enter the number of rows desired: ",
                    "Please enter the number of columns desired: ",
                    "Invalid size! Please retry with a size of minimum of 1 squares and maximum of 40 squares"
                
                    ]

