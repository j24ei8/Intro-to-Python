# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle:

  def __init__(self, max_speed, mileage):
    self.max_speed = max_speed
    self.mileage = mileage


modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)
print(modelX)

# Write a Python program to create a TrainTicket class with destination, time and price instance attributes.


class TrainTicket:

  def __init__(self, destination, time, price):
    self.destination = destination
    self.time = time
    self.price = price


modelY = TrainTicket("광명", 710, 8000)
print(modelY.destination, modelY.time, modelY.price)
