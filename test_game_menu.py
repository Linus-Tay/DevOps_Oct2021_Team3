
import unittest
import testBase
import sys 
from io import StringIO
import buildingPools 
import city
import gameMenu
default_pool = buildingPools.initBuildingPools('BCH','FAC','HSE','SHP','HWY')
default_map = city.newGrid(4,4)

class test_MainMenu_function(unittest.TestCase):
    def test_GameMenuInvOptAndOpt0(self):
        out = StringIO()
        sys.stdout = out 
        testBase.set_keyboard_input(["InvalidInput","0"])
        gameMenu.gameMenu(default_pool,default_map,1,"FAC","SHP")
        output = testBase.get_display_output()
        assert output == ["\n-----------------------Turn 1-----------------------\n",
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
                            
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See Current Score\n",
                            "[4] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? ",
                            "\nInvalid option, please try again",
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
                                
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See Current Score\n",
                            "[4] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? "]

    def test_GameMenuOpt3(self):
            out = StringIO()
            sys.stdout = out 
            testBase.set_keyboard_input(["3",'0'])
            gameMenu.gameMenu(default_pool,default_map,1,"FAC","SHP")
            output = testBase.get_display_output()
            assert output == [
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
                        
                        "[1] Build a FAC",
                        "[2] Build a SHP",
                        "[3] See Current Score\n",
                        "[4] Save Game",
                        "[0] Exit to main menu",
                        "\nYour Choice? ",
                        "Option 3, View Current Score!",
                        "\n-------------------Current Score--------------------\n",
                        "HSE: 0",
                        "FAC: 0",
                        "SHP: 0",
                        "HWY: 0",
                        "BCH: 0 ",
                        "\nTotal Score: 0",
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
                          
                          "[1] Build a FAC",
                          "[2] Build a SHP",
                          "[3] See Current Score\n",
                          "[4] Save Game",
                          "[0] Exit to main menu",
                          "\nYour Choice? "
            ]
    def test_GameMenuOpt4(self):
            out = StringIO()
            sys.stdout = out 
            testBase.set_keyboard_input(["4"])
            try:
              gameMenu.gameMenu(default_pool,default_map,1,"FAC","SHP")
            except:
                output = testBase.get_display_output()
                assert output[-1] == "Option 4, save game!"

    def test_EndGame(self):
      self.assertEqual(gameMenu.gameMenu(default_pool,default_map,17,"FAC","SHP"),"End") 

                             
