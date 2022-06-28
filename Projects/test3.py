# Syed Aftaabuddin
# Project 3a
# May 5, 2020
#Create list from file

from vehicle import Vehicle
fin = open("vehicles.txt", "r")

fin.readline( )

vehicle_info = [ ]
for line in fin:
           fields = line.strip( ).split(",")
           vin = fields[0]
           year = int(fields[1])
           color = fields[2]
           owner = fields[3]
           v = Vehicle(vin, year, color, owner)
           vehicle_info.append(v)
           
for v in vehicle_info:
    print(v)

