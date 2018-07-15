class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    def drive_car(self):
      self.condition = "used"

    def display_car(self):
        print "This is a %s %s with " % (self.color, self.model) + str(self.mpg) + " MPG."

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
    def drive_car(self):
      self.condition = "like new"


my_car = Car("DeLorean", "silver", 88)

print my_car.model
print my_car.color
print my_car.mpg

my_car.display_car()

print my_car.condition
my_car.drive_car()
print my_car.condition

my_care = ElectricCar("bmw", "red", 100, "molten salt")
print my_care.condition
my_care.drive_car()
print my_care.condition


class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print my_point


