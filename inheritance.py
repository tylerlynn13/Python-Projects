Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Truck:
    make = 'Ford'
    fuel = 'Gas'
    mileage = '234,456'

    
class Semi(Truck):
    cab = 'None'
    load_limit = '20,000'

    
class Pickup(Truck):
    bed = 'Long'
    4_wheel = 'Yes'