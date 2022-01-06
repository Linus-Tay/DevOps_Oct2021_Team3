from numpy.lib.utils import info
from gameMenu import gameMenu
from unittest import mock, TestCase
from testBase import get_display_output, set_keyboard_input
import sys 
from io import StringIO
import numpy as np
import buildingPools 
import city

class test_MainMenu_function(TestCase):
    def test_GameMenuInvOptAndOpt0(self):
        out = StringIO()
        sys.stdout = out 
        set_keyboard_input(["InvalidInput","0"])
        gameMenu(buildingPools.initBuildingPools,city.loadCity('start.csv'),1,"FAC","SHP")
        output = get_display_output()
        assert output == ["\n-----------------------Turn 1-----------------------\n",
                            "    A     B     C     D   ",
                            " +-----+-----+-----+-----+",
                            "1|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            "2|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            "3|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            "4|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            '',
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? ",
                            "\nInvalid option, please try again",
                            "\n-----------------------Turn 1-----------------------\n",
                            "    A     B     C     D   ",
                            " +-----+-----+-----+-----+",
                            "1|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            "2|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            "3|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            "4|     |     |     |     |",
                            " +-----+-----+-----+-----+",
                            '',
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? "]
    def test_GameMenuOpt3(self):
            out = StringIO()
            sys.stdout = out 
            set_keyboard_input(["3"])
            try:
              gameMenu(buildingPools.initBuildingPools,city.loadCity('start.csv'),1,"FAC","SHP")
            except:
                output = get_display_output()
                assert output[-2] + output[-1] == "Option 3, View Remaining Building Available!" + 'Buildings\tRemaining\n----------\t----------'
    def test_GameMenuOpt4(self):
            out = StringIO()
            sys.stdout = out 
            set_keyboard_input(["4","0"])
            gameMenu(buildingPools.initBuildingPools,city.loadCity('start.csv'),1,"FAC","SHP")
            output = get_display_output()
            assert output == [ "\n-----------------------Turn 1-----------------------\n",
                                "    A     B     C     D   ",
                                " +-----+-----+-----+-----+",
                                "1|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "2|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "3|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "4|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                '',
                                "[1] Build a FAC",
                                "[2] Build a SHP",
                                "[3] See remaining buildings",
                                "[4] See Current Score\n",
                                "[5] Save Game",
                                "[0] Exit to main menu",
                                "\nYour Choice? ",
                                "Option 4, Development in progress!",
                                "\n-----------------------Turn 1-----------------------\n",
                                "    A     B     C     D   ",
                                " +-----+-----+-----+-----+",
                                "1|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "2|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "3|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                "4|     |     |     |     |",
                                " +-----+-----+-----+-----+",
                                '',
                                "[1] Build a FAC",
                                "[2] Build a SHP",
                                "[3] See remaining buildings",
                                "[4] See Current Score\n",
                                "[5] Save Game",
                                "[0] Exit to main menu",
                                "\nYour Choice? "]

    def test_GameMenuOpt5(self):
            out = StringIO()
            sys.stdout = out 
            set_keyboard_input(["5"])
            try:
              gameMenu(buildingPools.initBuildingPools,city.loadCity('start.csv'),1,"FAC","SHP")
            except:
                output = get_display_output()
                assert output[-1] == "Option 5, save game!"

                             