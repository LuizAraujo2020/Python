#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors  = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my ", self.enginetype, " car at ", self.speed)
        
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hasSidecar):
        super().__init__("Motorcycle")
        if (hasSidecar):
            self.wheels = 3
        else:
            self.doors  = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my ", self.enginetype, " motorcycle at ", self.speed)

car1 = Car("gas")
car2 = Car("diesel")
car3 = Car("electric")

motorcycle1 = Motorcycle("gas", True)
motorcycle2 = Motorcycle("electric", False)

print(motorcycle1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
motorcycle1.drive(50)