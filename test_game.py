import unittest
from main import get_player1_number, provide_feedback, play_game

class TestGuessTheNumber(unittest.TestCase):

    def test_get_player1_number_valid(self):
        self.assertEqual(get_player1_number(50), 50)
    
    def test_get_player1_number_invalid_low(self):
        with self.assertRaises(ValueError):
            get_player1_number(0)

    def test_get_player1_number_invalid_high(self):
        with self.assertRaises(ValueError):
            get_player1_number(101)

    def test_provide_feedback_too_low(self):
        self.assertEqual(provide_feedback(30, 50), "Too low!")

    def test_provide_feedback_too_high(self):
        self.assertEqual(provide_feedback(70, 50), "Too high!")

    def test_provide_feedback_correct(self):
        self.assertEqual(provide_feedback(50, 50), "Correct!")

    


if __name__ == "__main__":
    unittest.main()
