import loadSavedGame
import buildingPools
import saveGame
import unittest

class test_saveGame_function(unittest.TestCase):
    def test_saveGame(self):
        mockCity = loadSavedGame.loadSavedGame('mockGame')
        mockbPool = buildingPools.initBuildingPools()
        saveGame.saveGame(mockCity,mockbPool,17,"BCH","FAC")
class test_loadSavedGame_functions(unittest.TestCase):
    # Test for Load Saved Game
    def test_if_Saved_Game_is_present(self):
        self.assertTrue(loadSavedGame.loadSavedGame('savedGame'))

    def test_if_Saved_Game_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedGame('fake'),'')

    # Test for Load Saved BuildingPools
    def test_if_loadSavedBuildingPools_is_present(self):
        results = loadSavedGame.loadSavedBuildingPools('savedBuildingPools')
        self.assertEqual(results["Building"][0],"BCH")
        self.assertEqual(results["Copies"][0],8)
        self.assertEqual(results["Building"][1],"FAC")
        self.assertEqual(results["Copies"][1],8)
        self.assertEqual(results["Building"][2],"HSE")
        self.assertEqual(results["Copies"][2],8)
        self.assertEqual(results["Building"][3],"SHP")
        self.assertEqual(results["Copies"][3],8)
        self.assertEqual(results["Building"][4],"HWY")
        self.assertEqual(results["Copies"][4],8)

    def test_if_loadSavedBuildingPools_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedBuildingPools('fake'),'')

    # Test for Load Saved Buildings
    def test_if_loadSavedBuildings_is_present(self):
        results = loadSavedGame.loadSavedBuildings('savedBuildings')
        self.assertEqual(results[0],"BCH")
        self.assertEqual(results[-1],"FAC")

    def test_if_loadSavedBuildings_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedBuildings('fake'),'') 
   
    # Test for Load Saved Turns
    def test_if_Saved_Turns_is_present(self):
        self.assertTrue(loadSavedGame.loadSavedTurns('savedTurns'))
    def test_if_Saved_Turns_is_not_present(self):
        self.assertEqual(loadSavedGame.loadSavedTurns('fake'),'') 
