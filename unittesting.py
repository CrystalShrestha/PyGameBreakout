import unittest
from breakouttwo import *


class TestHighScore(unittest.TestCase):
    """Testing high score"""

    def test_highscore(self):
        self.assertEqual(highestScore.HighestScore(self), '12')

    def test_events(self):
        self.assertEqual(Game.check_events(self), True)

if __name__ == '__main__':
    unittest.main()
