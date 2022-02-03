import sys
from city import newGrid
import main
import unittest
from io import StringIO
import filecmp

from testBase import get_display_output, set_keyboard_input

class test_MainMenu_function(unittest.TestCase):
    def test_MainMenu_Opt1(self):
        set_keyboard_input(['1'])
        try:
            main.mainMenu()
        except:
            output = get_display_output()
            assert output[6] == "Option 1 - Start New Game"

    def test_MainMenu_Opt2(self):
        set_keyboard_input(['2'])
        main.mainMenu()
        output = get_display_output()
        assert output[6] == "Option 2 - Load Save Game"

    def test_MainMenu_Opt0(self):
        set_keyboard_input(['0'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "[3] Building Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "All building settings resetted to default! See you again"]
        default_map = 'defaultmap.csv'
        default_pool = 'defaultpool.csv'
        play_map = 'playmap.csv'
        play_pool = 'playpool.csv'
        
        self.assertTrue(filecmp.cmp(default_map,play_map))
        self.assertTrue(filecmp.cmp(default_pool,play_pool)   )             



    def test_MainMenu_InvalidOpt(self):
        set_keyboard_input(['123'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "[3] Building Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            '\nInvalid option, please try again!']

    def test_BuildingSettingsMenu(self):
        out = StringIO()
        sys.stdout = out 
        set_keyboard_input(['3','0'])
        main.mainMenu()
        output = get_display_output()

        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "[3] Building Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "\nOption 3 - Building Settings",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "[0] Return to previous menu",
                            "\nEnter your choice? ",
        ]

    def test_BuildingSetting_Op1(self):
        out = StringIO()
        sys.stdout = out 
        set_keyboard_input(['3','1','5','5','0','0','0'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "[3] Building Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 3 - Building Settings",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "[0] Return to previous menu",
                            "\nEnter your choice? ",
                            "Choose City size with dimension of row and column",
                            "Please enter the number of rows desired: ",
                            "Please enter the number of columns desired: ",
                            "Your city map is now 5x5: ",
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
                            "[1] re-configure city map",
                            "[0] return to previous menu",
                            "Enter your choice?",
                            "Option 3 - Building Settings",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "[0] Return to previous menu",
                            "\nEnter your choice? ",
        ]






    def test_BuildingSetting_Op2(self):
        out = StringIO()
        sys.stdout = out 
        set_keyboard_input(['3','2'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "[3] Building Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 3 - Building Settings",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "[0] Return to previous menu",
                            "\nEnter your choice? ", 
                            "Choose your buildings",
                            "Available Buildings:\n",
                            "[1] Beach (BCH)",
                            "[2] Factory (FAC)",
                            "[3] House (HSE)",
                            "[4] Shop (SHP)",
                            "[5] Highway (HWY)",
                            "[6] Monuments (MON)",
                            "[7] Parks (PRK)",
                            "\nPlease choose your building (number) from the given options:",
                            "Your current list: (PRK)",
                            "Available Buildings:\n",
                            "[1] Beach (BCH)",
                            "[2] Factory (FAC)",
                            "[3] House (HSE)",
                            "[4] Shop (SHP)",
                            "[5] Highway (HWY)",
                            "[6] Monuments (MON)",
                            "\nPlease choose your building (number) from the given options:",
                            "Your current list: (PRK,HWY)",
                            "Available Buildings:\n",
                            "[1] Beach (BCH)",
                            "[2] Factory (FAC)",
                            "[3] House (HSE)",
                            "[4] Shop (SHP)",
                            "[5] Monuments (MON)",
                            "\nPlease choose your building (number) from the given options:",
                            "Your current list: (PRK,HWY,BCH)",
                            "Available Buildings:\n",
                            "[1] Factory (FAC)",
                            "[2] House (HSE)",
                            "[3] Shop (SHP)",
                            "[4] Monuments (MON)",
                            "\nPlease choose your building (number) from the given options:",
                            "Your current list: (PRK,HWY,BCH,SHP)",
                            "Available Buildings:\n",
                            "[1] Factory (FAC)",
                            "[2] House (HSE)",
                            "[3] Monuments (MON)",
                            "\nPlease choose your building (number) from the given options:",
                            "Your final list: (PRK,HWY,BCH,SHP,HSE)",  
                             "\nOption 3 - Building settings",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "[0] Return to previous menu",
                            "\nEnter your choice? ",
        ]


    # def test_BuildingSettingsMenu(self):
    #     #set_keyboard_input(['3','3','1','5','5','0','2','7','5','1','3','2','1','0'])
    #     out = StringIO()
    #     sys.stdout = out 
    #     set_keyboard_input(['3','1','5','5','0','2','7','5','1','3'])
    #     main.mainMenu()
    #     output = get_display_output()
    #     b1 = output[99]
    #     b2 = output[100]
    #     assert output == ["\nWelcome, mayor of Simp City!",
    #                         "----------------------------",
    #                         "[1] Start new game",
    #                         "[2] Load saved game",
    #                         "[3] Building Settings",
    #                         "\n[0] Exit",
    #                         "\nEnter your choice? ",
    #                         "\nOption 3 - Building settings",
    #                         "[1] Choose City Size",
    #                         "[2] Choose Building Pool",
    #                         "[0] Return to main menu",
    #                         "\nEnter your choice? ", 
    #                         "Choose City size with dimension of row and column",
    #                         "Please enter the number of rows desired: ",
    #                         "Please enter the number of columns desired: ",
    #                         "Your city map is now 5x5: ",
    #                         "     A     B     C     D     E   \t\tBuildings\tRemaining",
    #                         "  +-----+-----+-----+-----+-----+\t\tBCH\t\t8",
    #                         " 1|     |     |     |     |     |\t\tFAC\t\t8",
    #                         "  +-----+-----+-----+-----+-----+\t\tHSE\t\t8",
    #                         " 2|     |     |     |     |     |\t\tSHP\t\t8",
    #                         "  +-----+-----+-----+-----+-----+\t\tHWY\t\t8",
    #                         " 3|     |     |     |     |     |",
    #                         "  +-----+-----+-----+-----+-----+",
    #                         " 4|     |     |     |     |     |",
    #                         "  +-----+-----+-----+-----+-----+",
    #                         " 5|     |     |     |     |     |",
    #                         "  +-----+-----+-----+-----+-----+",
    #                         "[1] re-configure city map",
    #                         "[0] return to previous menu",
    #                         "Enter your choice?",
    #                         "\nOption 3 - Building settings",
    #                         "[1] Choose City Size",
    #                         "[2] Choose Building Pool",
    #                         "[0] Return to main menu",
    #                         "\nEnter your choice? ", 
    #                         "Choose your buildings",
    #                         "Available Buildings:\n",
    #                         "[1] Beach (BCH)",
    #                         "[2] Factory (FAC)",
    #                         "[3] House (HSE)",
    #                         "[4] Shop (SHP)",
    #                         "[5] Highway (HWY)",
    #                         "[6] Monuments (MON)",
    #                         "[7] Parks (PRK)",
    #                         "\nPlease choose your building (number) from the given options:",
    #                         "Your current list: (PRK)",
    #                         "Available Buildings:\n",
    #                         "[1] Beach (BCH)",
    #                         "[2] Factory (FAC)",
    #                         "[3] House (HSE)",
    #                         "[4] Shop (SHP)",
    #                         "[5] Highway (HWY)",
    #                         "[6] Monuments (MON)",
    #                         "\nPlease choose your building (number) from the given options:",
    #                         "Your current list: (PRK,HWY)",
    #                         "Available Buildings:\n",
    #                         "[1] Beach (BCH)",
    #                         "[2] Factory (FAC)",
    #                         "[3] House (HSE)",
    #                         "[4] Shop (SHP)",
    #                         "[5] Monuments (MON)",
    #                         "\nPlease choose your building (number) from the given options:",
    #                         "Your current list: (PRK,HWY,BCH)",
    #                         "Available Buildings:\n",
    #                         "[1] Factory (FAC)",
    #                         "[2] House (HSE)",
    #                         "[3] Shop (SHP)",
    #                         "[4] Monuments (MON)",
    #                         "\nPlease choose your building (number) from the given options:",
    #                         "Your current list: (PRK,HWY,BCH,SHP)",
    #                         "Available Buildings:\n",
    #                         "[1] Factory (FAC)",
    #                         "[2] House (HSE)",
    #                         "[3] Monuments (MON)",
    #                         "\nPlease choose your building (number) from the given options:",
    #                         "Your final list: (PRK,HWY,BCH,SHP,HSE)",  
    #                         "\nWelcome, mayor of Simp City!",
    #                         "----------------------------",
    #                         "[1] Start new game",
    #                         "[2] Load saved game",
    #                         "[3] Building Settings",
    #                         "\n[0] Exit",
    #                         "\nEnter your choice? ",
    #                         "Option 1 - Start New Game",
    #                         "\n-----------------------Turn 1-----------------------\n",
    #                         "     A     B     C     D     E   \t\tBuildings\tRemaining",
    #                         "  +-----+-----+-----+-----+-----+\t\tPRK\t\t8",
    #                         " 1|     |     |     |     |     |\t\tHWY\t\t8",
    #                         "  +-----+-----+-----+-----+-----+\t\tBCH\t\t8",
    #                         " 2|     |     |     |     |     |\t\tSHP\t\t8",
    #                         "  +-----+-----+-----+-----+-----+\t\tHSE\t\t8",
    #                         " 3|     |     |     |     |     |",
    #                         "  +-----+-----+-----+-----+-----+",
    #                         " 4|     |     |     |     |     |",
    #                         "  +-----+-----+-----+-----+-----+",
    #                         " 5|     |     |     |     |     |",
    #                         "  +-----+-----+-----+-----+-----+",
    #                         "[1] Build a" + b1[11:15],
    #                         "[2] Build a" + b2[11:15],
    #                         "[3] See remaining buildings",
    #                         "[4] See Current Score\n",
    #                         "[5] Save Game",
    #                         "[0] Exit to main menu",
    #                         "\nYour Choice? "                              
    #                         ]
