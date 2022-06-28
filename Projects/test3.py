# Syed Aftaabuddin
# Project 3c
# Due Date: 5/22/2020
# Submission Date: 5/21/2020


# importing Automobile class from automobiles.py file
from automobiles import Automobile

#Create empty dictionary
auto_dict = { }

#Open input file
fin1 = open("automobiles.txt", "r")

#Throw away first line
fin1.readline( )

for line in fin1:
    fields = line.strip( ).split(",")
    vin = fields[0]
    year = int(fields[1])
    make = fields[2]
    color = fields[3]
    owner = fields[4]
    model = fields[5]
    num_cylinders = fields[6]
    a = Automobile(vin, year, make, color, owner, model, num_cylinders)
    auto_dict[fields[0]] = a

#printing out the dictionary
print(auto_dict) 

# open accessories.txt file
fin2 = open("accessories.txt", "r")
for line in fin2:
    fields = line.strip( ).split(",")
    vin = fields.pop(0)
    for a in fields:
        auto_dict[vin].add_accessories(a)


while True:       
    search_vin = input("Enter vin please: " )

    if search_vin in auto_dict:
        a = auto_dict[search_vin]
        print("Owner: ", a.owner)
        print("Make: ", a.make)
        print("Model: ", a.model)
        print("Year: ", a.year)
        print("Color: ", a.color)
        print("Cylinders: ", a.num_cylinders)
        print("Miles: ", a.miles)
        print("Accessories: ", a.accessories)
    else:
        print("Automobile not in dictionary")
