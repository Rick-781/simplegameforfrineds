import unittest
from main import get_player1_number, provide_feedback, play_game

class TestGuessTheNumber(unittest.TestCase):

    def test_get_player1_number_valid(self):
        self.assertEqual(get_player1_number(50), 50)


if __name__ == "__main__":
    unittest.main()