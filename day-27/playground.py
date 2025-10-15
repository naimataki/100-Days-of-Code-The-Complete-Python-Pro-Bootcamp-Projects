# Unlimited Postional arguments
def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1, 2, 3, 7, 8, 9, 20, 21, 33))

def calculate(n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)

    #print(kwargs["add"])

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw['make']
        #self.model = kw['model']
        self.model = kw.get("model") # if no model value it returns None
        self.color = kw.get("color")
        self.seats = kw.get("seats")

#my_car = Car(make='Nissan', model='GT-R')
my_car = Car(make='Nissan')
print(my_car.make)
print(my_car.model)
