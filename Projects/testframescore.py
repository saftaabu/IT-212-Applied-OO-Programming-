# Filename: testframescore.py
import unittest
from framescore import frame_score

class TestFrameScore(unittest.TestCase):

    def test_1(self):
        self.assertEqual(frame_score([10], 10, 7), 27)

    def test_2(self):
        self.assertEqual(frame_score([7, 3], 9, 0), 19)

    def test_3(self):
        self.assertEqual(frame_score([7, 1], 0, 0), 8)

if __name__ == '__main__':
    unittest.main()
