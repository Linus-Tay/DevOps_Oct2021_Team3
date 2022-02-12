import unittest

import highScore
from testBase import get_display_output, set_keyboard_input

# Pre-Set 10x10.csv Highscores
# Test Addition of High Score
class Add_High_Score_function(unittest.TestCase):
    def test_adding_score(self):
        highScores = [['test',100],['test',100],['test',100],['test',100],['test',100],
              ['test',100],['test',100],['test',100]]
        dimension = ["10","10"]
        playerScore = 100
        set_keyboard_input(['test'])
        highScore.addHighScore(dimension,playerScore,highScores)
        set_keyboard_input([''])
        highScore.displayHighScore(dimension)
        output = get_display_output()
        assert output == [
            '\n--------- HIGH SCORES ---------',
            'Pos Player                Score',
            '--- ------                -----',
            ' 1. test                    100',
            ' 2. test                    100',
            ' 3. test                    100',
            ' 4. test                    100',
            ' 5. test                    100',
            ' 6. test                    100',
            ' 7. test                    100',
            ' 8. test                    100',
            ' 9. test                    100',
            '\n'
        ]

# Test Dislay High Score Function
class Display_High_Score_function(unittest.TestCase):
    # Positive Test Case
    def test_with_actual_dimension(self):
        dimension = ["10","10"]
        set_keyboard_input([''])
        highScore.displayHighScore(dimension)
        output = get_display_output()
        assert output == [
            '\n--------- HIGH SCORES ---------',
            'Pos Player                Score',
            '--- ------                -----',
            ' 1. test                    100',
            ' 2. test                    100',
            ' 3. test                    100',
            ' 4. test                    100',
            ' 5. test                    100',
            ' 6. test                    100',
            ' 7. test                    100',
            ' 8. test                    100',
            ' 9. test                    100',
            '\n'
        ]

    # Negative Test Case
    def test_with_false_dimension(self):
        dimension = ["10","11"]
        set_keyboard_input([''])
        highScore.displayHighScore(dimension)
        output = get_display_output()
        assert output == ['\nCurrently, there is not high score set for city size 10x11.\n']

# Test High Score List Function
class Get_HS_List_function(unittest.TestCase):
    # Positive Test Case
    def test_with_actual_dimension_Positive(self):
        dimension = ["10","10"]
        results = [['test',100],['test',100],['test',100],['test',100],['test',100],
                   ['test',100],['test',100],['test',100],['test',100]]
        self.assertEqual(highScore.getHSList(dimension),results)
    
    # Negative Test Case
    def test_with_false_dimension_Negative(self):
        dimension = ["10","11"]
        self.assertEqual(highScore.getHSList(dimension),[])

# Test Take Second Function
class Take_Second_function(unittest.TestCase):
    # Positive Test Case
    def test_with_positive_data(self):
        data = ["test",100]
        self.assertEqual(highScore.takeSecond(data),100)
    
    # Negative Test Case
    def test_with_negative_data(self):
        data = ["test"]
        self.assertEqual(highScore.takeSecond(data),'')  

# Test Print Headers Function
class Print_Headers_function(unittest.TestCase):
    # Positive Test Case
    def test_printing_Positive(self):
        set_keyboard_input([''])
        highScore.printHeaders()
        output = get_display_output()
        assert output == [
            '\n--------- HIGH SCORES ---------',
            'Pos Player                Score',
            '--- ------                -----'
        ]
    # No Negative Test Case as its just printing with no params involve

# Test Check High Score Function
class Check_High_Score_function(unittest.TestCase):
    # Positive Test Cases
    # When High Score List has less than 10 positions,
    # Whatever Player scores, it will be added to High Score List
    def test_check_for_less_than_10_position(self):
        dimension = ["10","10"]
        playerScore = 90
        set_keyboard_input(['PlayerName'])
        highScore.checkHighScore(dimension,playerScore)
        highScore.displayHighScore(dimension)
        output = get_display_output()
        assert output == [
            'Please enter your name (max 20 chars): ',
            '\n--------- HIGH SCORES ---------',
            'Pos Player                Score',
            '--- ------                -----',
            ' 1. test                    100',
            ' 2. test                    100',
            ' 3. test                    100',
            ' 4. test                    100',
            ' 5. test                    100',
            ' 6. test                    100',
            ' 7. test                    100',
            ' 8. test                    100',
            ' 9. test                    100',
            '10. PlayerName               90',
            '\n'
        ]

    # When High Score List has 10 positions,
    # Player scores higher than the scores in the high score list
    def test_with_higher_player_score(self):
        dimension = ["10","10"]
        playerScore = 95
        set_keyboard_input(['PlayerName'])
        highScore.checkHighScore(dimension,playerScore)
        highScore.displayHighScore(dimension)
        output = get_display_output()
        assert output == [
            'Please enter your name (max 20 chars): ',
            '\n--------- HIGH SCORES ---------',
            'Pos Player                Score',
            '--- ------                -----',
            ' 1. test                    100',
            ' 2. test                    100',
            ' 3. test                    100',
            ' 4. test                    100',
            ' 5. test                    100',
            ' 6. test                    100',
            ' 7. test                    100',
            ' 8. test                    100',
            ' 9. test                    100',
            '10. PlayerName               95',
            '\n'
        ]
    
    # Player scores the same as the lowest score in the high score list
    def test_with_same_player_score(self):
        dimension = ["10","10"]
        playerScore = 95
        set_keyboard_input([''])
        highScore.checkHighScore(dimension,playerScore)
        output = get_display_output()
        assert output == [
            "\nUnfortunately, you didn't make it to the High Score List. The minimum score required is {}.".format(playerScore + 1)
        ]

    # Player scores lower than the scores in the high score list 
    def test_with_lower_player_score(self):
        dimension = ["10","10"]
        playerScore = 90
        set_keyboard_input([''])
        highScore.checkHighScore(dimension,playerScore)
        output = get_display_output()
        assert output == [
            "\nUnfortunately, you didn't make it to the High Score List. The minimum score required is 96."
        ]

    # Test with Invalid parameters - Negative Test Case
    def test_with_negative_dimension(self):
        dimension = ["10",10]
        playerScore = 80
        set_keyboard_input([''])
        highScore.checkHighScore(dimension,playerScore)
        output = get_display_output()
        assert output == [
            "An error occured, parameters for checkHighScore function is invalid."
        ]

    def test_with_negative_player_score(self):
        dimension = ["10","10"]
        playerScore = "80"
        set_keyboard_input([''])
        highScore.checkHighScore(dimension,playerScore)
        output = get_display_output()
        assert output == [
            "An error occured, parameters for checkHighScore function is invalid."
        ]


