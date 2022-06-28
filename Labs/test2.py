# Syed Aftaabuddin
# Lab 2
# April 27, 2020


from clock import Clock
import unittest

class MyUnitTestClass(unittest.TestCase):

    def test_1(self):
        c = Clock(4, 7, 3)
        self.assertEqual(str(c), '04:07:03')
        self.assertEqual(c.hr, 4)
        self.assertEqual(c.min, 7)
        self.assertEqual(c.sec, 3)
        c.tick(  )
        self.assertEqual(str(c), '04:07:04')

    def test_2(self):
        c = Clock(4, 7, 59)
        self.assertEqual(str(c), '04:07:59')
        c.tick(  )
        self.assertEqual(str(c), '04:08:00')
        
    def test_3(self):
        c = Clock(4, 59, 59)
        self.assertEqual(str(c), '04:59:59')
        c.tick(  )
        self.assertEqual(str(c), '05:00:00')
        
    def test_4(self):
        c = Clock(23, 59, 59)
        self.assertEqual(str(c), '23:59:59')
        c.tick(  )
        self.assertEqual(str(c), '00:00:00')
        


if __name__ == '__main__':
    unittest.main( )


    
