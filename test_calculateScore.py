import unittest
import loadSavedGame
import calculateScore

class test_ViewCurrentScore_function(unittest.TestCase):
    def test_ScoreCalculation(self):
        mockCity = loadSavedGame.loadSavedGame('./mockGames/mockGame')
        self.assertEqual(calculateScore.calculateScore(mockCity),50)
        mockCity2 = loadSavedGame.loadSavedGame('./mockGames/mockGame2')
        self.assertEqual(calculateScore.calculateScore(mockCity2),48)
        mockCity3 = loadSavedGame.loadSavedGame('./mockGames/mockGame3')
        self.assertEqual(calculateScore.calculateScore(mockCity3),19)
        mockCity4 = loadSavedGame.loadSavedGame('./mockGames/mockGame4')
        self.assertEqual(calculateScore.calculateScore(mockCity4),18)

class test_Calculate_Park_Building(unittest.TestCase):
    def test_calculate_0_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'FAC', 'A2': 'FAC', 'A3': 'FAC', 'A4': 'HWY',
                'B1': 'FAC', 'B2': 'FAC', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'FAC', 'D2': 'BCH', 'D3': 'HSE', 'D4': 'MON'}
        self.assertEqual(calculateScore.calculatePRK(dict),0)
    def test_calculate_1_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'FAC', 'A3': 'FAC', 'A4': 'HWY',
                'B1': 'FAC', 'B2': 'FAC', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'FAC', 'D2': 'BCH', 'D3': 'HSE', 'D4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),2)

    def test_calculate_2_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'FAC', 'A3': 'FAC', 'A4': 'HWY',
                'B1': 'PRK', 'B2': 'FAC', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'FAC', 'D2': 'BCH', 'D3': 'PRK', 'D4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),6)


    def test_calculate_3_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'HWY',
                'B1': 'FAC', 'B2': 'FAC', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'FAC', 'D2': 'PRK', 'D3': 'PRK', 'D4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),16)

    def test_calculate_4_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK',
                'B1': 'FAC', 'B2': 'FAC', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'PRK', 'C4': 'PRK',
                'D1': 'FAC', 'D2': 'BCH', 'D3': 'PRK', 'D4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),32)

    def test_calculate_5_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK',
                'B1': 'PRK', 'B2': 'FAC', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'PRK', 'C4': 'PRK',
                'D1': 'FAC', 'D2': 'PRK', 'D3': 'PRK', 'D4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),44)

    def test_calculate_6_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK',
                'B1': 'PRK', 'B2': 'PRK', 'B3': 'FAC', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'PRK', 'D2': 'PRK', 'D3': 'HSE', 'D4': 'MON',
                'E1': 'PRK', 'E2': 'PRK', 'E3': 'PRK', 'E4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),46)
    
    def test_calculate_7_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK',
                'B1': 'PRK', 'B2': 'PRK', 'B3': 'PRK', 'B4': 'HWY',
                'C1': 'FAC', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'PRK', 'D2': 'PRK', 'D3': 'PRK', 'D4': 'HWY',
                'E1': 'PRK', 'E2': 'PRK', 'E3': 'PRK', 'E4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),48)
    
    def test_calculate_8_park(self):
        # MOCK DATA FOR TESTING
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK',
                'B1': 'PRK', 'B2': 'PRK', 'B3': 'PRK', 'B4': 'PRK',
                'C1': 'HWY', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'PRK', 'D2': 'PRK', 'D3': 'PRK', 'D4': 'PRK',
                'E1': 'PRK', 'E2': 'PRK', 'E3': 'PRK', 'E4': 'PRK'}
        self.assertEqual(calculateScore.calculatePRK(dict),50)

class test_Calculate_Monument_Building(unittest.TestCase):
    def test_MON_calculation(self):
        dict = {'A1': 'MON', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK',
                'B1': 'PRK', 'B2': 'PRK', 'B3': 'PRK', 'B4': 'PRK',
                'C1': 'HWY', 'C2': 'FAC', 'C3': 'FAC', 'C4': 'HWY',
                'D1': 'PRK', 'D2': 'PRK', 'D3': 'PRK', 'D4': 'MON',
                'E1': 'PRK', 'E2': 'PRK', 'E3': 'PRK', 'E4': 'MON'}
        dimension = ["4","5"]
        self.assertEqual(calculateScore.calculateMON(dict,dimension),12)
    def test_with_1x1_dimension(self):
        dimension = ["1","1"]
        dict = {'A1': 'MON'}
        self.assertEqual(calculateScore.calculateMON(dict,dimension),2)
    def test_with_10x1_dimension(self):
        dimension = ["10","1"]
        dict = {'A1': 'PRK', 'B1': 'MON', 'C1': 'PRK', 'D1': 'PRK','E1': 'PRK',
                 'F1': 'PRK', 'G1': 'PRK', 'H1': 'PRK', 'I1': 'PRK', 'J1': 'MON'}
        self.assertEqual(calculateScore.calculateMON(dict,dimension),3)
    def test_with_MON_not_in_corners(self):
        dimension = ["1","10"]
        dict = {'A1': 'PRK', 'A2': 'MON', 'A3': 'PRK', 'A4': 'PRK','A5': 'PRK',
                 'A6': 'PRK', 'A7': 'PRK', 'A8': 'PRK', 'A9': 'PRK', 'A10': 'PRK'}
        self.assertEqual(calculateScore.calculateMON(dict,dimension),1)

    def test_with_no_MON(self):
        dimension = ["1","10"]
        dict = {'A1': 'PRK', 'A2': 'PRK', 'A3': 'PRK', 'A4': 'PRK','A5': 'PRK',
                 'A6': 'PRK', 'A7': 'PRK', 'A8': 'PRK', 'A9': 'PRK', 'A10': 'PRK'}
        self.assertEqual(calculateScore.calculateMON(dict,dimension),0)
# pytest test_calculateScore.py --html=report.html --self-contained-html