#########################################################
# Name: William Wilson
# Date: 2021-1-22
# Description: Implements vehicle, truck and car classes.
#########################################################

# the vehicle class
# a vehicle has a year, make, and model
# a vehicle is instantiated with a make and model

class Vehicle():
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if(value > 2000 and value < 2018):
            self._year = value
        else:
            self._year = 2000

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    def __str__(self):
        return ("{} {} {}".format(self.year, self.make, self.model))
 
# the truck class
# a truck is a vehicle
# a truck is instantiated with a make and model

class Truck(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, year, make, model) 
        

# the car class
# a car is a vehicle
# a car is instantiated with a make and model

class Car(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)

# the Dodge Ram class
# a Dodge Ram is a truck
# a Dodge Ram is instantiated with a year
# all Dodge Rams have the same make and model

class DodgeRam(Vehicle):
    make = "Dodge"
    model = "Ram"
    def __init__(self, year):
        Vehicle.__init__(self, year, DodgeRam.make, DodgeRam.model)

# the Honda Civic class
# a Honda Civic is a car
# a Honda Civic is instantiated with a year
# all Honda Civics have the same make and model

class HondaCivic(Car):
    make = "Honda"
    model = "Civic"
    def __init__(self, year):
        Vehicle.__init__(self, year, HondaCivic.make, HondaCivic.model)
        
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
ram = DodgeRam(2016)
print(ram)

civic1 = HondaCivic(2007)
print(civic1)

civic2 = HondaCivic(1999)
print(civic2)
