from gameMenu import gameMenu
import main
from unittest import mock, TestCase
from testBase import get_display_output, set_keyboard_input
import sys 
from io import StringIO
import numpy as np
import buildingPools 
import city

class test_MainMenu_function(TestCase):
    def test_GameMenuOpt(self):
        out = StringIO()
        sys.stdout = out 
        set_keyboard_input(["3","4","5","InvalidInput","0"])
        gameMenu(buildingPools.initBuildingPools,city.loadCity('start.csv'),1,"FAC","SHP")
        output = get_display_output()
        assert output == ["\n-----------------------Turn 1-----------------------\n",
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? ",
                            "Option 3, Development in progress!",
                            "\n-----------------------Turn 1-----------------------\n",
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? ",
                            "Option 4, Development in progress!",
                            "\n-----------------------Turn 1-----------------------\n",
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? ",
                            "Option 5, Development in progress!",
                            "\n-----------------------Turn 1-----------------------\n",
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? ",
                            "\nInvalid option, please try again",
                            "\n-----------------------Turn 1-----------------------\n",
                            "[1] Build a FAC",
                            "[2] Build a SHP",
                            "[3] See remaining buildings",
                            "[4] See Current Score\n",
                            "[5] Save Game",
                            "[0] Exit to main menu",
                            "\nYour Choice? "]
    