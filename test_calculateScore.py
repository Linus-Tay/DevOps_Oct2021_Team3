import unittest
import loadSavedGame
import calculateScore

class test_ViewCurrentScore_function(unittest.TestCase):
    def test_ScoreCalculation(self):
        mockCity = loadSavedGame.loadSavedGame('mockGame')
        self.assertEqual(calculateScore.calculateScore(mockCity),50)
        mockCity2 = loadSavedGame.loadSavedGame('mockGame2')
        self.assertEqual(calculateScore.calculateScore(mockCity2),48)
        mockCity3 = loadSavedGame.loadSavedGame('mockGame3')
        self.assertEqual(calculateScore.calculateScore(mockCity3),20)
# pytest test_calculateScore.py --html=report.html --self-contained-html