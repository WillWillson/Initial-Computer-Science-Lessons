###########################################################################
# Name:William Wilson
# Date:01/01/21
# Description: This program should give the year, make and model for different vehicles.
###########################################################################

# the vehicle class
# a vehicle has a year, make and model
class Vehicle:

    def __init__(self, make, model):

        self.make = make
        self.model = model
        
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
print("v1={} {}".format(v1.make, v1.model))
print("v2={} {}".format(v2.make, v2.model))
print()

v1.year = 2016
v2.year = 2016
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))
print()

v1.year = 1999
v2.model = "Civic"
v2.year = 2007
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))

             
