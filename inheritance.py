class Truck:
    make = 'Ford'
    fuel = 'Gas'
    mileage = 234,456
#this is the parent class
    
class Semi(Truck):
    cab = None
    load_limit = 20,000
#first child class
    
class Pickup(Truck):
    bed = 'Long'
    four_wheel = 'Yes'
#second child class
