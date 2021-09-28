import unittest
import mongodb


class TestHighScore(unittest.TestCase):

    # Connecting to the monogo DB
    '''def test_high_score(self):
        data = mongodb.fetch_high_score()
        self.assertEqual(data.get('score'), 9)'''

    def test_low_score(self):
        data = mongodb.fetch_low_score()
        self.assertEqual(data.get('score'), 2)


if __name__ == '__main__':
    unittest.main()
