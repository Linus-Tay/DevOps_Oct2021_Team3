import unittest
import loadSavedGame

class test_loadSavedGame_function(unittest.TestCase):
    def test_if_Saved_Game_is_present(self):
        self.assertTrue(loadSavedGame.loadSavedGame('savedGame'))
    def test_if_Saved_Game_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedGame('fake'),'')

class test_loadSavedBuildingPools_function(unittest.TestCase):
    def test_if_loadSavedBuildingPools_is_present(self):
        results = loadSavedGame.loadSavedBuildingPools('savedBuildingPools')
        self.assertEqual(results["Building"][0],"BCH")
        self.assertEqual(results["Building"][1],"FAC")
        self.assertEqual(results["Building"][2],"HSE")
        self.assertEqual(results["Building"][3],"SHP")
        self.assertEqual(results["Building"][4],"HWY")
    def test_if_loadSavedBuildingPools_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedBuildingPools('fake'),'')

class test_loadSavedTurns_function(unittest.TestCase):
    def test_if_Saved_Turns_is_present(self):
        self.assertTrue(loadSavedGame.loadSavedTurns('savedTurns'))
    def test_if_Saved_Turns_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedBuildingPools('fake'),'')
        