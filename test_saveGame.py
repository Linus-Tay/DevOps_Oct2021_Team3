import loadSavedGame
import buildingPools
import saveGame
import unittest

class test_saveGame_function(unittest.TestCase):
    def test_saveGame(self):
        mockCity = loadSavedGame.loadSavedGame('mockGame')
        mockbPool = buildingPools.initBuildingPools()
        saveGame.saveGame(mockCity,mockbPool,1)
        self.assertTrue(loadSavedGame.loadSavedGame('savedGame'))
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
        self.assertTrue(loadSavedGame.loadSavedTurns('savedTurns'))
