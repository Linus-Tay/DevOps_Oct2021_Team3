import main
import unittest

class test_MainMenu_function(unittest.TestCase):
    def test_MainMenu(self):
        print("\nTest MainMenu\nStart")
        self.assertTrue(main.mainMenu())
        print("\nEnd")

if __name__ == "__main__":
    unittest.main()