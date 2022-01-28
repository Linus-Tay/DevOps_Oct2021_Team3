import main
import unittest
from testBase import get_display_output, set_keyboard_input

class test_MainMenu_function(unittest.TestCase):
    def test_MainMenu_Opt1(self):
        set_keyboard_input(['1'])
        try:
            main.mainMenu()
        except:
            output = get_display_output()
            assert output[7] == "Option 1 - Start New Game"

    def test_MainMenu_Opt2(self):
        set_keyboard_input(['2'])
        main.mainMenu()
        output = get_display_output()
        assert output[7] == "Option 2 - Load Save Game"

    def test_MainMenu_Opt3(self):
        set_keyboard_input(['3','1','2'])
        main.mainMenu()
        output = get_display_output()
        assert output[7] == "\nOption 3 - Show High Scores\n"

    def test_MainMenu_Opt3_Invalid_Dimension(self):
        set_keyboard_input(['3','10','10'])
        main.mainMenu()
        output = get_display_output()
        assert output[7:10] == ["\nOption 3 - Show High Scores\n",
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
                            "\n[0] Exit",
                            "\nEnter your choice? "]
                            
    def test_MainMenu_InvalidOpt(self):
        set_keyboard_input(['123'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start New Game",
                            "[2] Load Saved Game",
                            '[3] Show High Scores',
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            '\nInvalid option, please try again!']