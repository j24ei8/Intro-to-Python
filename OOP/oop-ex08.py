# Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle:

  def __init__(self, max_speed, mileage):
    self.max_speed = max_speed
    self.mileage = mileage


modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)


class Primestone:

  def __init__(self, max_hour, lecture, teacher, student, gender, age):
    self.max_hour = max_hour
    self.lecture = lecture
    self.teacher = teacher
    self.student = student
    self.__gender = gender
    self.__age = age


python_lecture = Primestone(2.5, 2, "Rosalyn", "Julie", "Female", 15)
print(python_lecture.max_hour, python_lecture.lecture, python_lecture.teacher,
      python_lecture.student, python_lecture.__gender, python_lecture.__age)
