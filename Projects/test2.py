#Syed Aftaabuddin
#5/14/2020
#Unit Test for Project 3b


#importing Automobile class from automobiles.py file
from automobiles import Automobile
import unittest

class MyUnitTestClass(unittest.TestCase):

 #creating a function called test_automobile to test       
   def test_automobile(self):
        a = Automobile('R7682T',2011,'Red','Ted','Infinity','Q70', 8)
        self.assertEqual(str(a),
                         "R7682T 2011 Red Ted Infinity Q70 8")
        self.assertEqual(a.make, "Infinity")
        self.assertEqual(a.model , "Q70")
        self.assertEqual(a.num_cylinders , 8)
        self.asserEqual(a.miles, 0)
        a.add_accessories("Mat")
        a.add_accessories("Seat Cover")
        a.add_accessories("Tyres")
        self.assertEqual(a.accessories, ["Mat", "Seat Cover", "Tyres"])
        
     
        
if __name__ == '__main__':
    unittest.main( )

 
        
