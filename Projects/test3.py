# Syed Aftaabuddin
# Project 3b
# May 14, 2020
#Create list from file

#Importing Automobile Class from automobiles.py file

from automobiles import Automobile
fin = open("automobiles.txt", "r")

#Throw away first line
fin.readline( )

autos = [ ] 
for line in fin:
           fields = line.strip( ).split(",")
           vin = fields[0]
           year = int(fields[1])
           make = fields[2]
           color = fields[3]
           owner = fields[4]
           model = fields[5]
           num_cylinders = fields[6]

           
           a = Automobile(vin, year, make, color, owner, model, num_cylinders)
           autos.append(a) #appending a information in autos list
           
print(autos)  #printing unsorted list first        
fin.close( )  #closing the file
autos.sort( ) #sorting out the list by owners name
print(autos)  #printing final sorted list

