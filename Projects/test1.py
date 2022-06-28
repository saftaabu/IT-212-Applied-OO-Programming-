#Syed Aftaabuddin
#5/14/2020
#Traditional Test for Project 3b

#importing Automobile class from automobiles.py file
from automobiles import Automobile

a = Automobile('R7682T',2011,'Red','Ted','Infinity','Q70',8)

print(a)


print( )

a.add_accessories('Mat')
a.add_accessories('Seat Cover')
a.add_accessories('Tyres')
a.add_miles(100)

#adding accessories and miles
print("Adding Accessories: ", a.accessories)
print("Adding Miles: ", a.miles)

print( )

#printing out the test to make sure accessories and miles are added
print(a)
