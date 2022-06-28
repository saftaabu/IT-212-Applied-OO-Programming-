# Syed Aftaabuddin
# Project 3b
# May 13, 2020

#importing Vehicle from vehicle.py file
from vehicle import Vehicle

class Automobile(Vehicle):

    def __init__(self, vin, year, color, owner, make, model, num_cylinders, miles=0):
        super().__init__(vin, year, color, owner)
        self.make = make
        self.model = model
        self.num_cylinders = num_cylinders
        self.miles = miles
        self.accessories = []
#created a function to add miles 
    def add_miles(self, the_miles):
        self.miles+= the_miles

    def add_accessories(self, the_item):
        self.accessories.append(the_item)

    def __str__(self):
        desc = 'Make: {}, Model: {}, Cylinders: {}, Miles: {}, Accessories: {}'
        desc = desc.format(self.make,self.model,self.num_cylinders,self.miles, ', '.join(self.accessories))
        return super().__str__()+desc


    def __repr__(self):
        return self.__str__()

    #Add __It__ method to make the list of Automobile sortable
    def __lt__(self, other):
        return self.owner < other.owner



