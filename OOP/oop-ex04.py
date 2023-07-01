# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.


class Vehicle:

  def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage


class Bus(Vehicle):

  def seating_capacity(self):
    self.capacity = 50


# modelX = Bus(50)
# print(modelX)

#####
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed,
      "Mileage:", School_bus.mileage)

# print(School_bus.capacity)
School_bus.seating_capacity()
print("School bus capacity:", School_bus.capacity)
