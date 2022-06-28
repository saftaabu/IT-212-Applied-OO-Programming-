# Syed Aftaabuddin
# Project 3a
# May 5, 2020

from datetime import datetime
class Vehicle:
    

    def __init__(self, vin, year, color, owner):
        
        #coverted to uppercase
        vin = vin.upper( )
        
        #if year greater than current_year
        current_year = datetime.now( ).year
        if year > current_year:
            year = current_year
            
        #removing all special characters from vin
        alphanumeric_filter = filter(str.isalnum, vin)
        self.vin = "".join(alphanumeric_filter)
        self.year = year
        self.color = color
        self.owner = owner
        self._sales_tax_paid = False
         

    def is_sales_tax_paid(self):
        if self._sales_tax_paid:
            return "Yes"
        else:
            return "No"
        
    def pay_sales_tax(self):
        self._sales_tax_paid = True


    def __str__(self):
        ret_val = f"Vin: {self.vin}\n" + \
            f"Year: {self.year}\n" + \
            f"color: {self.color}\n" + \
            f"Owner: {self.owner}\n" + \
            f"Is Sales Tax Paid: {self.is_sales_tax_paid( )}\n"
        return ret_val


    def __repr__(self):
        return str(self)



