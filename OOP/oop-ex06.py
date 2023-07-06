class Polygon:

  def __init__(self, side, length):
    self.side = side
    self.length = length

  def area(self):
    print("The area of the polygon is...")


class Circle(Polygon):

  def area(self):
    print("The area of the circle is...")


poly = Polygon(3, 7)
poly.area()
cir = Circle(0, 3)
cir.area()
