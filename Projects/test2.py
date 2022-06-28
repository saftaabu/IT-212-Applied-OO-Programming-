# Syed Aftaabuddin
# Project 3a
# May 5, 2020
#Unit Test

from vehicle import Vehicle
import unittest

class MyUnitTestClass(unittest.TestCase):
        
    def test_vehicle(self):
        p3 = Vehicle("M1032F", 2018, "gold", "susan")
        self.assertEqual(str(p3), \
'''Vin: M1032F
Year: 2018
color: gold
Owner: susan
Is Sales Tax Paid: No
''')
        self.assertEqual(p3.vin, "M1032F")
        self.assertEqual(p3.year, 2018)
        self.assertEqual(p3.color, "gold")
        self.assertEqual(p3.owner, "susan")
        self.assertEqual(p3.is_sales_tax_paid( ), "No")
        p3.pay_sales_tax( )
        self.assertEqual(p3.is_sales_tax_paid( ), "Yes")
        
        
if __name__ == '__main__':
    unittest.main( )
