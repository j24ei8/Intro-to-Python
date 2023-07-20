# Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.


class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width 

  def multiplication(self):
    product = self.length * self.width
    return product 

modelX = Rectangle(4,12)
print(modelX.multiplication())
