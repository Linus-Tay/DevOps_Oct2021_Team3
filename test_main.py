import filecmp
import main
import unittest
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
        set_keyboard_input(['3','1','2'])
        main.mainMenu()
        output = get_display_output()
        assert output[8] == "\nOption 3 - Show High Scores\n"

    def test_MainMenu_Opt3_Invalid_Dimension(self):
        set_keyboard_input(['3','10','10'])
        main.mainMenu()
        output = get_display_output()
        assert output[8:11] == ["\nOption 3 - Show High Scores\n",
                                "Please enter the number of rows desired: ",
                                "Please enter the number of columns desired: "]
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
