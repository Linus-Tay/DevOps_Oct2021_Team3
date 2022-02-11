import filecmp
import main
import unittest
from io import StringIO
import filecmp

from testBase import get_display_output, set_keyboard_input

class test_MainMenu_function(unittest.TestCase):
    def test_MainMenu_Opt1(self):
        set_keyboard_input(['1','0'])
        try:
            main.mainMenu()
        except:
            output = get_display_output()
            assert output[7] == "Option 1 - Start New Game"

    def test_MainMenu_Opt2(self):
        set_keyboard_input(['2','0'])
        main.mainMenu()
        output = get_display_output()
        assert output[8] == "Option 2 - Load Save Game"

    def test_MainMenu_Opt3(self):
        set_keyboard_input(['3','0','0'])
        main.mainMenu()
        output = get_display_output()
        assert output[8] == "\nOption 3 - Show High Scores\n"

    def test_MainMenu_Opt3_View_Other_City_Highscore_Invalid_Dimension(self):
        set_keyboard_input(['3','1','10','10','0','0'])
        main.mainMenu()
        output = get_display_output()
        assert output[15] == "\nDimension entered is invalid!"

    def test_MainMenu_Opt0(self):
        set_keyboard_input(['0'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start New Game",
                            "[2] Load Saved Game",
                            '[3] Show High Scores',
                            "[4] Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
        ]
                            
    def test_MainMenu_InvalidOpt(self):
        set_keyboard_input(['123','0'])
        main.mainMenu()
        output = get_display_output()
        # there should be a sub-menu in "Option 3 - Building Settings"
        # function should print as expected
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start New Game",
                            "[2] Load Saved Game",
                            '[3] Show High Scores',
                            "[4] Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            '\nInvalid option, please try again!']

    # test case "Option 4 - Building Settings" in main menu
    def test_BuildingSettingsMenu(self):
        set_keyboard_input(['4','0'])
        main.mainMenu()
        output = get_display_output()
        # there should be a sub-menu in "Option 3 - Building Settings"
        # function should print as expected
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start New Game",
                            "[2] Load Saved Game",
                            '[3] Show High Scores',
                            "[4] Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
                            "\nEnter your choice? ",
        ]

    #test case for "[1] choose city size" in "Building Settings"    
    def test_BuildingSetting_Op1(self):

        set_keyboard_input(['4','1','5','5','0','0','0'])
        main.mainMenu()
        output = get_display_output()
        # the process of choosing city size should run when user selects it
        # function should return to "Building Settings" 
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start New Game",
                            "[2] Load Saved Game",
                            '[3] Show High Scores',
                            "[4] Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
                            "\nEnter your choice? ",
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
                            "Enter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
                            "\nEnter your choice? ",
        ]

    def test_BuildingSetting_Op2(self):
        set_keyboard_input(['4','2','7','5','1','3','2','0','0'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            '[3] Show High Scores',
                            "[4] Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
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
                            "Enter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
                            "\nEnter your choice? ",
        ]
    def test_BuildingSetting_reconfig(self):
        set_keyboard_input(['4','2','7','5','1','3','2','1','7','5','1','3','2','0','0'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            '[3] Show High Scores',
                            "[4] Settings",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
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
                            "Enter your choice? ",
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
                            "Enter your choice? ",
                            "Option 4 - Settings\n",
                            "[1] Choose City Size",
                            "[2] Choose Building Pool",
                            "\n[0] Return to main menu",
                            "\nEnter your choice? ",
        ]
