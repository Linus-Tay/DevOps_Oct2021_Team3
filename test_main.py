import main
import unittest
from testBase import get_display_output, set_keyboard_input

class test_MainMenu_function(unittest.TestCase):
    def test_MainMenu_Opt1(self):
        set_keyboard_input(['1'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 1 - Start New Save Game"]
    def test_MainMenu_Opt2(self):
        set_keyboard_input(['2'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "Option 2 - Load Save Game"]
    def test_MainMenu_Opt0(self):
        set_keyboard_input(['0'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            "\nThank you for playing Simp City!\n"]
    def test_MainMenu_InvalidOpt(self):
        set_keyboard_input(['123'])
        main.mainMenu()
        output = get_display_output()
        assert output == ["\nWelcome, mayor of Simp City!",
                            "----------------------------",
                            "[1] Start new game",
                            "[2] Load saved game",
                            "\n[0] Exit",
                            "\nEnter your choice? ",
                            '\nInvalid option, please try again!']