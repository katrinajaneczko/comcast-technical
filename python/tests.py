import unittest
import io, sys
from app import *

class TestStringinator(unittest.TestCase):

    def test_mostFrequentChar(self):
        input = 'Comcast is the best place to work!'
        expected = 4 #'t' appears 4 times
        actual = mostFrequentChar(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
