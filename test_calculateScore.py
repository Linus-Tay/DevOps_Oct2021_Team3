import unittest
import loadSavedGame
import calculateScore

class test_ViewCurrentScore_function(unittest.TestCase):
    def test_ScoreCalculation(self):
        mockCity = loadSavedGame.loadSavedGame('mockGame')
        self.assertEqual(calculateScore.calculateScore(mockCity),50)

# pytest test_calculateScore.py --html=report.html --self-contained-html