# Syed Aftaabuddin
# Project 3a
# May 5, 2020
#Traditional Test

from vehicle import Vehicle

#creating test case
#testing p1 vin as it removes all non-digit/non-letter

p1 = Vehicle("R##$76!!82T", 2011, "red", "Ted")
p2 = Vehicle("Z5211W", 2015, "silver", "Elaine")
p3 = Vehicle("M1032F", 2018, "gold", "susan")
p4 = Vehicle("S0987F", 2017, "black", "Fred")
p5 = Vehicle("N3128B", 2017, "black", "Fred")
p6 = Vehicle("N3129B", 2020, "white", "Oscar")
p7 = Vehicle("U3813W", 2013, "blue", "Stephanie")
p8 = Vehicle("C4921Y", 2015, "red", "Morgan")
p9 = Vehicle("D5019H", 2019, "yellow", "William")
p10 = Vehicle("R1235T", 2017, "silver", "Alice")
p11 = Vehicle("W9632D", 2019, "green", "Mary")


a = [ ]
a.append(p1)
a.append(p2)
a.append(p3)
a.append(p4)
a.append(p5)
a.append(p6)
a.append(p7)
a.append(p8)
a.append(p9)
a.append(p10)
a.append(p11)

for p in a:
    print(p)

#pay sales tax for p1 
p1.pay_sales_tax()

#checking if sales tax paid for p1
print("Is sales tax paid for p1: ", p1.is_sales_tax_paid())

#testing non-digit/non-letter characters for p1
#R7!!68$$2##T should out R7682T
print("Testing vin by removing all non digits/non-letter:", p1.vin)
